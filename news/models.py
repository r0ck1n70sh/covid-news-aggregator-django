from django.db import models

class Article(models.Model):
    title= models.CharField(max_length=200)
    publishedAt= models.DateTimeField('date published')
    author= models.CharField(max_length=200)
    source= models.CharField(max_length=200)
    description= models.TextField(max_length=200)

    url=models.URLField(max_length=200)
    image= models.URLField(max_length=200)

    def __str__(self):
        return self.title

class LastUpdate(models.Model):
    date= models.DateField()

    def __str__(self):
        return self.date.strftime("%Y-%m-%d")
