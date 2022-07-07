from django.contrib import admin
from .models import *
# Register your models here.



class NewsAdmin(admin.ModelAdmin):
    list_display = ['title', 'text', 'date']

admin.site.register(News, NewsAdmin)