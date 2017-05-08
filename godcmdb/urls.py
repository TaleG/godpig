# _*_ coding:utf-8 _*_
from django.conf.urls import url,include
from godcmdb import views

urlpatterns = [
    url(r'^server_cmdb_list/', views.server_cmdb_list,name='server_cmdb_list'),
    url(r'^asset_cmdb_list/', views.asset_cmdb_list,name='asset_cmdb_list'),
    url(r'^godcmdb/server_cmdb_list_info/$', views.server_cmdb_list_info,name='server_cmdb_list_info'),
]
