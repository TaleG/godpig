from django.shortcuts import render
from godcmdb import models
# Create your views here.

def server_cmdb_list(request):
    server_cmdb_obj = models.Server.objects.all()
    return render(request,'cmdb/Server_cmdb.html',{'server_cmdb_obj':server_cmdb_obj})