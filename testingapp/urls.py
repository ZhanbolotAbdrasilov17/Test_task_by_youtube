from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import *


urlpatterns = [
    path('', IndexView.as_view(), name='index'),
]