from django.db import models
from django.contrib.auth.models import User
from django.utils.html import format_html
from django.utils import timezone
# Create your models here.

class UserProfile(models.Model):
    user = models.OneToOneField(User)
    name = models.CharField(u'名字',max_length=32)
    user_code = models.IntegerField(u'代码')
    # user_name = models.CharField(u'姓名',max_length=200)
    user_type = models.CharField(u'用户类型 ',max_length=10,null=True,blank=True)
    user_group = models.CharField(u'值班小组',max_length=1,null=True,blank=True)
    user_group2 = models.CharField(u'二线小组',max_length=1,null=True,blank=True)
    user_group_role= models.CharField(u'组角色',max_length=5,null=True,blank=True)
    user_grade= models.IntegerField(u'等级',null=True,blank=True)
    user_company = models.CharField(u'所在公司',max_length=30,null=True,blank=True)
    user_role_id = models.IntegerField(u'角色',null=True,blank=True)
    user_phone= models.IntegerField(u'联系电话',null=True,blank=True)
    user_email = models.CharField(u'邮箱',null=True,blank=True,max_length=20)
    user_address = models.CharField(u'籍贯',null=True,blank=True,max_length=50)
    user_pswd= models.CharField(u'签到密码',max_length=200,null=True,blank=True)
    open_date= models.DateTimeField(u'入职日期',auto_now = True,null=True,blank=True)
    user_status = models.CharField(u'状态', max_length=1, null=True, blank=True)
    remark = models.CharField(u'备注',max_length=100,null=True,blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name='用户'
        verbose_name_plural='用户管理'

#签到
class check_day(models.Model):
    check_name= models.ForeignKey(UserProfile,verbose_name=u'签到人')
    check_date= models.DateField(u'签到日期',auto_now=True)
    checkin_time = models.DateTimeField(u'签入时间',null=True,blank=True)
    checkout_time = models.DateTimeField(u'签出时间',null=True,blank=True)
    class Meta:
        unique_together=('check_name','check_date')
        verbose_name='签到'
        verbose_name_plural='签到管理'

    def __str__(self):
        check_date_str= str(self.check_date)
        return check_date_str

#字典
class sys_dd_item(models.Model):
    dd_id = models.CharField(U'字段',max_length=20)
    dd_item=models.CharField(U'字段值',max_length=5,unique=True)
    dd_item_name = models.CharField(u'名称',max_length=100)
    def __str__(self):
        return self.dd_id
    class Meta:

        unique_together = ('dd_id', 'dd_item')
        verbose_name='字典'
        verbose_name_plural='字典管理'


#值班列表
class schedule(models.Model):
    sys_year = models.DateField(u'值班日期',default=timezone.now)
    month = models.CharField(u'月份',max_length=5)
    day = models.CharField(u'日',max_length=5)
    dule_group_type = (
        ("A",u'A组'),
        ("B",u"B组"),
        ("C",u"C组"),
        ("D",u"D组"),
    )
    date_flag_type=(
        ('0',u"非交易日"),
        ('1',u"交易日")
                    )
    west_day_type = (
        ('星期一',u'星期一'),
        ('星期二',u'星期二'),
        ('星期三',u'星期三'),
        ('星期四',u'星期四'),
        ('星期五',u'星期五'),
        ('星期六',u'星期六'),
        ('星期日',u'星期日'),

                    )
    date_flag = models.CharField(u'交易日',choices=date_flag_type,max_length=10)
    west_day = models.CharField(u'星期', choices=west_day_type,max_length=50)
    dule_group = models.CharField(u'值班小组',choices=dule_group_type,max_length=24,null=True,blank=True)
    remark = models.CharField(max_length=200,null=True,blank=True)
    show_times = models.CharField(u'周次数',max_length=5)
    class Meta:
        verbose_name='值班'
        verbose_name_plural='值班管理'

    def __str__(self):
        date=str(self.sys_year)
        return date
    def colored_name(self):
        return format_html(
            '<span style="color: red {};">{} {}</span>',
            self.dule_group,
            self.date_flag,
        )

#加班统计
class restdays(models.Model):
    wrecordmen_type=(
        ('周经纬',u'周经纬'),
        ('陈茂华',u'陈茂华'),
        ('曹强',u'曹强'),
        ('李纯', u'李纯'),
    )
    wweek_type=(
        ('星期一',u'星期一'),
        ('星期二',u'星期二'),
        ('星期三',u'星期三'),
        ('星期四',u'星期四'),
        ('星期五',u'星期五'),
        ('星期六',u'星期六'),
        ('星期日',u'星期日'),
    )
    wtimes_type=(
        ('1',u'1天'),
        ('0.5',u'0.5天'),
    )
    wrecordmen=models.CharField(u'登记人',choices=wrecordmen_type,max_length=20)
    wweek=models.CharField(u'星期',choices=wweek_type,max_length=20)
    wdate=models.DateField(u'日期',default=timezone.now)
    wmen=models.CharField(u'加班人员',max_length=50)
    wtimes=models.CharField(u'加班时长',choices=wtimes_type,max_length=20)
    wcontent=models.CharField(U'加班事项',max_length=200)
    def __str__(self):
            return str(self.wdate)
    class Meta:
        verbose_name='加班'
        verbose_name_plural='加班管理'

class god_sign(models.Model):
    pass