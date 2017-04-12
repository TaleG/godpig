from django.shortcuts import render
from projectpig import models
from projectpig import form
from django.shortcuts import render,HttpResponseRedirect,HttpResponse
from django.contrib.auth import login,logout,authenticate
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger

# Create your views here.

#项目登记
def Projectpig(request):
    project_list = models.Projectpig.objects.all()
    return render(request, 'Projectpig/project_list.html', {'project_list':project_list})

#添加项目登记
def new_article(request):
    if request.method == 'GET':
        article_form = form.ArticleModelForm()
        return render(request,'Projectpig/project_add.html',{'article_form':article_form})
    elif request.method == "POST":
        print(request.POST)
        if request.method == 'POST':
            new_article_obj = models.Projectpig(
                project_name = request.POST.get('project_name'),
                person_in_charge = request.POST.get('person_in_charge'),
                work_content = request.POST.get('work_content'),
                open_date = request.POST.get('open_date'),
                end_type = request.POST.get('end_type'),
                end_date = request.POST.get('end_date'),
            )
            new_article_obj.save()
        return HttpResponseRedirect(request.GET.get('next') or '/Projectpig')

        # article_form = form.ArticleModelForm(request.POST)
        # if article_form.is_valid():
        #     article_form.save()
        #     return HttpResponse("ok")
        # else:
        #     return render(request,'Projectpig/project_add.html',{'article_form':article_form})

def new_article_list(request):
    new_article_list_obj = models.Projectpig.objects.all()
    return render(request, 'Projectpig/new_article_list.html', {"new_article_list_obj":new_article_list_obj})

#项目跟踪
def project_fault(request):
    project_fault_obj = models.Project_speed.objects.all()
    return render(request, 'Projectpig/project_fault.html',{"project_fault_obj":project_fault_obj})

#漏洞登记
def bug_fault(request):
    bug_fault_obj = models.bug_fault.objects.all()
    return render(request,'Projectpig/bug_fault.html',{"bug_fault_obj":bug_fault_obj})

# def customers(request):
#     customer_list = models.Projectpig.objects.all()
#
#     paginator = Paginator(customer_list,3)
#     page = request.GET.get('page')
#     try:
#         customer_objs = paginator.page(page)
#     except PageNotAnInteger:
#         customer_objs = paginator.page(1)
#     except EmptyPage:
#         customer_objs = paginator.page(paginator.num_pages)
#
#     return render(request,'Projectpig/project_list.html',{'customer_list':customer_objs})

def god_fault(request):
    god_fault_obj = models.god_bug.objects.all()
    return render(request, 'Projectpig/project_fault_list.html', {"god_fault_obj":god_fault_obj})


