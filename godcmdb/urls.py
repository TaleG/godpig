
from django.conf.urls import url,include
from godcmdb import views

urlpatterns = [
    url(r'^server_cmdb_list/', views.server_cmdb_list,name='server_cmdb_list'),
]
