from django.db import models
from django.utils import timezone
# Create your models here.

from godbody.models import UserProfile


#公告
class announcement(models.Model):
    create_time = models.DateTimeField(u'创建日期',default=timezone.now)
    announ_title= models.CharField(u'主题',default='',max_length=100)
    context = models.CharField(u'公告内容',max_length=300)
    exec_time = models.DateField(u'执行时间')
    sign_name=models.ForeignKey(UserProfile,verbose_name=u'登记人')
    remark = models.CharField(u'备注',max_length=300,null=True,blank=True)
    def __str__(self):
        return self.context
    class Meta:
        verbose_name='公告'
        verbose_name_plural='公告管理'

#券商列表
class secu_list(models.Model):
    id_for_com=models.IntegerField(u'id号',primary_key=True)
    name_for_com=models.CharField(u'券商',max_length=100)


    class Meta:
        verbose_name = '券商列表'
        verbose_name_plural = '券商列表'
    def __str__(self):
            return self.name_for_com
#渠道列表
class channel_list(models.Model):
        id_for_cha = models.IntegerField(u'id号', primary_key=True)
        name_for_cha = models.CharField(u'渠道列表', max_length=100)

        class Meta:
            verbose_name = '渠道列表'
            verbose_name_plural = '渠道列表'

        def __str__(self):
            return self.name_for_cha
#项目列表
class project(models.Model):
    pnum=models.CharField(u'编号',max_length=50)
    pjira=models.CharField(u'jira编号',max_length=30)
    pdate=models.DateField(u'登记日期',default=timezone.now,max_length=30)
    punit_type=(
        ('P0','其他'),
        ('P1','托管'),
        ('P2','互联网金融大开户'),
        ('P3','互联网金融独立开户'),
        ('P4','互联网金融独立交易'),
        ('P5','第三方'),
        ('P6','上海运营部（内部）'),

    )
    punit=models.CharField(u'项目类型',choices=punit_type,max_length=30)
    #pchannel=models.CharField(u'渠道',max_length=30)
    #psecur=models.CharField(u'券商',max_length=30)
    pname=models.CharField(u'项目名称',max_length=30)
    pdoc_type=(
        ('D0','其他'),
        ('D1','全新项目'),
        ('D2','追加渠道'),
    )
    pdoc=models.CharField(u'项目类别',choices=pdoc_type,max_length=30)
    pallot_type=(
        ('周经纬', u'周经纬'),
        ('陈茂华', u'陈茂华'),
        ('曹强', u'曹强'),
    )
    pallot=models.CharField(u'派工人',choices=pallot_type,max_length=30)
    pnetmen_type = (
        ('高大海', u'高大海'),
        ('崔飞', u'崔飞'),
        ('孙志崴', u'孙志崴'),
    )
    pstatus_type= (
        ('0',u'已验收'),
        ('1',u'实施中'),
        ('2',u'暂停'),
        ('3',u'上线'),
        ('4',u'关闭'),

    )
    pmen_type=(

    )
    pmen=models.CharField(u'项目经理',max_length=30)
    p_channel=models.ForeignKey(channel_list,related_name='ez_qd',)
    p_secu=models.ForeignKey(secu_list,related_name='ez_qs')
    pnetmen=models.CharField(u'平台人员',choices=pnetmen_type,max_length=30)
    ponliedate=models.DateField(u'上线日期')
    pstatus=models.CharField(u'项目状态',choices=pstatus_type,max_length=30)
    premark=models.CharField(u'备注',max_length=30)

    def __str__(self):
            return self.pnum
    class Meta:
        verbose_name='项目'
        verbose_name_plural='项目管理'

class planshows(models.Model):
    pstype=models.CharField(u'计划类型',max_length=10,null=True,blank=True)
    pstime=models.CharField(u'计划时间',max_length=10,null=True,blank=True)
    pstitle=models.CharField(u'计划主题',max_length=20,null=True,blank=True)
    psinfo=models.TextField(u'计划内容',max_length=200,null=True,blank=True)
    psremark=models.CharField(u'备注',max_length=100,null=True,blank=True)
    def __str__(self):
            return str(self.pstitle)
    class Meta:
        verbose_name='计划任务'
        verbose_name_plural='计划任务'
