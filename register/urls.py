from  django.conf .urls import include, url
from django.contrib import admin
from register.views import Home


urlpatterns =[
    url(r'^$',Home.as_view(),name='home'),

]