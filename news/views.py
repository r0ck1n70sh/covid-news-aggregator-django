from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.urls import reverse
from urllib.parse import urlencode

from datetime import date, timedelta

from .models import Article, LastUpdate

from .scrapper import scrapper

def index(request):
    lastUpdate= LastUpdate.objects.latest('date').date.strftime('%d %B %Y')

    message= request.GET.get('message')

    articles = Article.objects.order_by('-publishedAt')
    page = request.GET.get('page', 1)


    paginator = Paginator(articles, 5)
    try:
        article_list = paginator.page(page)
    except PageNotAnInteger:
        article_list = paginator.page(1)
    except EmptyPage:
        article_list= paginator.page(paginator.num_pages)


    context = {
        'article_list': article_list,
        'lastUpdate': lastUpdate,
        'message': message,
        }

    template= 'news/index.html'

    return render(request, template, context)


def updater(request):
    lastUpdate= LastUpdate.objects.latest('date').date

    base_url= reverse('index')

    if lastUpdate == date.today():
            query_string= urlencode({'message': 'error'})
            url= '{}?{}'.format(base_url, query_string)
            return redirect(url)

    new_article_list= scrapper(lastUpdate)
    lastUpdate= date.today()

    newUpdate= LastUpdate()
    newUpdate.date= lastUpdate
    newUpdate.save()

    for article in new_article_list:
        new_article= Article()

        new_article.title= article['title']
        new_article.author= article['author']
        new_article.source= article['source']['name']
        new_article.publishedAt= article['publishedAt']
        new_article.description= article['description']

        new_article.url= article['url']
        new_article.image= article['urlToImage']

        new_article.save()

    query_string = urlencode({'message': 'success'})
    url= '{}?{}'.format(base_url, query_string)

    return redirect(url)
