from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect
from django.conf import settings
# Create your views here.
from django.template import context
from .models import *
from .forms import  NewsForm
from django.views import View


class IndexView(View):

    def get(self, request):
        news = News.objects.all()
        form = NewsForm()
        context = {
            "news":news,
            "form":form,
        }
        return render(request, 'index.html',context)

    def post(self,request):
        form = NewsForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect('index')
        else:
            news = News.objects.all()
            context = {"news": news, "form": form}
            return render(request, 'index.html', context)