from django.shortcuts import render
from django.contrib.auth import login,logout,authenticate
from django.shortcuts import render,HttpResponseRedirect
from django.contrib.auth.decorators import login_required


# Create your views here.

def dashboard(request):

    return render(request,'monitor/dashboard.html')

def triggers(request):

    return render(request,'monitor/triggers.html')
@login_required
def index(request):
    return render(request,'start/index.html')


def acc_login(request):
    #用POST模式获取前端数据传来的数据
    if request.method == 'POST':
        print(request.POST)
        user = authenticate(username = request.POST.get('username'),
                            password = request.POST.get('password'),
                            )
        if user is not None:
            login(request,user)
            return HttpResponseRedirect(request.GET.get('next') or '/login')
        else:
            login_err = "Wrong username or password!"
            return render(request, 'start/login.html', {'login_err':login_err})
    return render(request, 'start/login.html')

def acc_sign(request):
    pass

def acc_logout(request):
    logout(request)
    return HttpResponseRedirect(request.GET.get('next') or '/login')
