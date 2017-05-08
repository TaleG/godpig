from django.shortcuts import render,HttpResponse
import os
import subprocess
# Create your views here.


def god_operation(request):
    ip_type = []
    # if request.method == 'POST':
    ips = request.POST.get('ipnub')
    # print(ips)
    status,nmap_put = subprocess.getstatusoutput("nmap %s"% ips)
    nmap_put_str = str(nmap_put)
    nmap_put_str_type = nmap_put_str.split('\n')

    for i in nmap_put_str_type:
        ip_type.append(i)
    #查看列表中某一个元素
    # print(nmap_put_str_type[0])
    # print(nmap_put_str_type[1])
    # print(nmap_put_str_type[2])
    # print(nmap_put_str_type[3])
    # print(nmap_put_str_type[4])

    # print(nmap_put_str_type[5])
    # print(nmap_put_str_type[6])
    # print(nmap_put_str_type[7])
    # print(nmap_put_str_type[8])
    # print(nmap_put_str_type[9])

    return render(request,'support/god_operation.html',{"ip_type":ip_type})
