"""godpig URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
from projectpig import views

urlpatterns = [


    url(r'^Projectpig/$', views.Projectpig,name='Projectpig'),
    url(r'^new_article/$', views.new_article,name='new_article'),
    # url(r'^new_article_list/(\d+)/$', views.new_article_list,name='new_article_list'),
    url(r'^new_article_list/$', views.new_article_list,name='new_article_list'),
    url(r'^god_fault/$', views.god_fault,name='god_fault'),
    url(r'^project_fault/$', views.project_fault,name='project_fault'),
    url(r'^bug_fault/$', views.bug_fault,name='bug_fault'),
]
