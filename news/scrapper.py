from newsapi import NewsApiClient
from datetime import date, timedelta

def scrapper(last_updated):

    today_date= date.today()

    if last_updated < today_date - timedelta(days=28):
        last_updated = today_date - timedelta(days=28)

    newsapi= NewsApiClient(api_key= '97b5d8d97d134421a5453ec84b629198')

    all_articles =newsapi.get_everything(
            q='covid AND india',
            from_param= last_updated,
            to= today_date,
            language='en',
            sort_by='relevancy',
        )


    articles= all_articles['articles']

    return articles

