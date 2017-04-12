from django.db import models
from django.contrib.auth.models import User
from godbody.models import UserProfile
# Create your models here.

class Projectpig(models.Model):
    project_name = models.CharField(u'项目名',max_length=64)
    person_in_charge = models.ForeignKey(UserProfile,verbose_name='负责人')
    work_content = models.TextField(u'工作内容',)
    open_date = models.DateField(u'开始时间')
    end_choices = (
        (0,'None'),
        (1,u'已完工'),
        (2,u'未完工')
    )
    end_type = models.IntegerField(u'完工状态',choices=end_choices,default=0,blank=True,null=True)
    end_date = models.DateField(u'结束时间',blank=True,null=True)

    def __str__(self):
        return self.work_content

class Project_speed(models.Model):
    article = models.ForeignKey(Projectpig,verbose_name=u"项目跟踪")
    project_track = models.TextField(u'工作进度')
    end_choices = (
        (0,'None'),
        (1,u'已完工'),
        (2,u'未完工')
    )
    end_type = models.IntegerField(u'完工状态',choices=end_choices,default=0,blank=True,null=True)
    name = models.ForeignKey(UserProfile,verbose_name='跟踪人员')
    Completion_date = models.DateField(u'完成时间',blank=True,null=True)
    expect_date = models.DateField(u'预期完成时间',blank=True,null=True)
    memo = models.TextField(u'备注',null=True,blank=True)

    def __str__(self):
        return self.project_track


class god_bug(models.Model):
    god_bug_date = models.DateTimeField(u'故障日期')
    god_bug_choices=(
        (1,u'系统'),
        (2,u'应用'),
        (3,u'网络')
    )
    god_bug_type = models.IntegerField(u'影响类别',choices=god_bug_choices,default=2)
    god_bug_ip = models.CharField(u'故障IP',max_length=32,blank=True,null=True)
    god_bug_phenomenon = models.TextField(u'故障现象')
    god_bug_solve = models.TextField(u'故障解决',blank=True,null=True)
    god_bug_track = models.TextField(u'故障跟踪',blank=True,null=True)
    god_bug_registrant = models.ForeignKey(UserProfile,verbose_name=u"登记人")
    god_bug_remarks = models.CharField(u'备注',max_length=64,blank=True,null=True)

    def __str__(self):
        return self.god_bug_ip

class bug_fault(models.Model):
    bug_code = models.CharField(u'漏洞代码',max_length=32)
    bug_name = models.CharField(u'漏洞名称',max_length=32)
    bug_version = models.CharField(u'漏洞影响版本',max_length=64)
    bug_synopsis = models.TextField(u'漏洞简介')
    bug_harm = models.TextField(u'漏洞危害')
    bug_repair_work_choices = (
        (1,u'已完成'),
        (2,u'未完成')
    )
    bug_repair_work = models.IntegerField(u'修复状况',choices=bug_repair_work_choices,default=1)
    bug_register_time = models.DateField(u"记录时间")
    bug_registrant = models.ForeignKey(UserProfile,verbose_name=u"登记人")
    memo = models.TextField(u'备注',null=True,blank=True)