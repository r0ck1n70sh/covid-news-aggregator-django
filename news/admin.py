from django.contrib import admin
from .models import Article, LastUpdate

admin.site.register(Article)
admin.site.register(LastUpdate)
