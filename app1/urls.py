from django.urls import path
from app1.views import *
app_name='somthing'
urlpatterns=[
    path('string1/',string1,name='string1'),
]