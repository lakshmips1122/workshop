from  django.conf .urls import include, url
from django.contrib import admin
from register.views import Home
from register import urls as reg_urls

urlpatterns =[
    url(r'^$',Home.as_view(),name='home'),

    url(r'^ register/', include(reg_urls)),

    url(r'^admin/',include(admin.site.urls)),

]