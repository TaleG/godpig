
from django.conf.urls import url,include
from godsupport import views

urlpatterns = [
    url(r'^god_operation/', views.god_operation,name='god_operation'),
]
