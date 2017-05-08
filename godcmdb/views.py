from django.shortcuts import render
from godcmdb.models import *
from godpig.api import *
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger

# Create your views here.

def server_cmdb_list(request):

    #搜索
    if request.method == 'POST':
        ips = request.POST.get('ipnmb')
        SearchResult = []
        server_cmdb_obj = Server.objects.all()
        for x in server_cmdb_obj:
            if ips in x.asset.management_ip:
                SearchResult.append(x)
            elif ips in x.IPS.ipaddress:
                SearchResult.append(x)
        SearchStatus = "Error" if len(SearchResult) == 0 else "Success"
        ResultAmount = len(SearchResult)
        return render(request,'cmdb/search.html',{'server_cmdb_obj':SearchResult,
                                                       'ResultAmount':ResultAmount,
                                                       'SearchStatus':SearchStatus
                                                       })
    #分页打印所有信息
    server_cmdb_obj = Server.objects.all()
    paginator = Paginator(server_cmdb_obj,7)
    page = request.GET.get('page')
    try:
        customer_objs = paginator.page(page)
    except PageNotAnInteger:
        customer_objs = paginator.page(1)
    except EmptyPage:
        customer_objs = paginator.page(paginator.num_pages)
    return render(request,'cmdb/Server_cmdb.html',{'server_cmdb_obj':customer_objs})

def asset_cmdb_list(request):
    asset_cmdb_list_obj = Asset.objects.all()
    return render(request, "cmdb/asset_cmdb_list.html", {"asset_cmdb_list_obj":asset_cmdb_list_obj})

#搜索功能
def server_cmdb_list_info(request):
    godcmdb_id = request.GET.get('id', '')
    # godcmdb = get_object(Server, id=godcmdb_id)
    godcmdb_record =Server.objects.filter(id=godcmdb_id)
    return render(request,'cmdb/server_cmdb_list_info.html',{'godcmdb_record':godcmdb_record})
