# _*_ coding:utf-8 _*_
from __future__ import unicode_literals
from django.db import models
from godbody.models import UserProfile


# Create your models here.


class Asset(models.Model):
    asset_type_choices = (('server',u'物理机'),
                          ('openstack',u'云虚拟机'),
                          ('switch',u'交换机'),
                          ('router',u'路由器'),
                          ('firewall',u'防火墙'),
                          ('storage',u'存储设备'),
                          ('NLB',u'负载均衡'),
                          ('wireless',u'无线AP'),
                          ('software',u'软件资产'),
                          ('others',u'其它类'),
                          )
    asset_type = models.CharField(choices=asset_type_choices,max_length=64,default='server',verbose_name=u'设备类型')
    name = models.CharField(u'设备名',max_length=64,unique=True,blank=True,null=True)
    sn = models.CharField(u'资产SN号',max_length=128,unique=True,blank=True,null=True)
    production_test_choices =(
        (1,u'生产'),
        (2,u'测试'),
    )
    production_test = models.IntegerField(verbose_name=u'生产／测试',choices=production_test_choices,default=1)
    model = models.CharField(u'机柜号',max_length=12,null=True,blank=True)
    model_position = models.CharField(u'机柜位置',max_length=12,null=True,blank=True)
    manufactory = models.ForeignKey('Manufactory',verbose_name=u'制造商',blank=True,null=True)
    os_type = models.ForeignKey('Software',verbose_name=u'系统类型',blank=True,null=True)
    cpu_info = models.ForeignKey('CPU',verbose_name=u'CPU信息')
    mem_info = models.ForeignKey('RAM',verbose_name=u'内存信息')
    disk_info = models.ForeignKey('Disk',verbose_name=u'磁盘信息')
    management_ip = models.GenericIPAddressField(u'管理IP',blank=True,null=True)
    ip1 = models.GenericIPAddressField(u"eth1",blank=True,null=True)
    ip2 = models.GenericIPAddressField(u"eth2",blank=True,null=True)
    ip3 = models.GenericIPAddressField(u"eth3",blank=True,null=True)
    ip4 = models.GenericIPAddressField(u"eth4",blank=True,null=True)
    raid_type = models.CharField(u'raid类型',max_length=512,blank=True,null=True)
    contract = models.ForeignKey('Contract',verbose_name=u'合同',null=True,blank=True)
    trade_data = models.DateField(u'购买时间',null=True,blank=True)
    expire_date = models.DateField(u'过保修期',null=True,blank=True)
    price = models.FloatField(u'价格',null=True,blank=True)
    business_unit = models.ForeignKey('BusinessUnit',verbose_name=u'所属项目',blank=True,null=True)
    admin = models.ForeignKey(UserProfile,verbose_name='管理员',blank=True,null=True)
    idc = models.ForeignKey('IDC',verbose_name=u'IDC机房',null=True,blank=True)
    memo = models.TextField(u'备注',null=True,blank=True)
    create_date = models.DateTimeField(blank=True,auto_now_add=True)
    update_date = models.DateTimeField(blank=True,auto_now=True)

    class meta:
        verbose_name = "资产总表"
        verbose_name_plural = "资产总表"
    def __str__(self):
        return 'id:%s name:%s' %(self.id,self.name)

class Server(models.Model):
    asset = models.ForeignKey('Asset')
    created_by_choices = (
        ('auto',u'自动'),
        ('manual','手动'),
        )
    created_by = models.CharField(choices=created_by_choices,max_length=32,default='manual',verbose_name=u'添加模式')
    hosted_on = models.ForeignKey('self',related_name='hosted_on_server',blank=True,null=True)
    business_unit = models.ForeignKey('BusinessUnit',verbose_name=u'所属项目',blank=True,null=True)
    cpu_info = models.ForeignKey('CPU',verbose_name=u'CPU信息')
    mem_info = models.ForeignKey('RAM',verbose_name=u'内存信息')
    disk_info = models.ForeignKey('Disk',verbose_name=u'磁盘信息')
    IPS = models.ForeignKey('NIC',verbose_name=u'网卡信息',blank=True,null=True)
    ips1 = models.GenericIPAddressField(u"eth1",blank=True,null=True)
    ips2 = models.GenericIPAddressField(u"eth2",blank=True,null=True)
    ips3 = models.GenericIPAddressField(u"eth3",blank=True,null=True)
    os_type = models.ForeignKey('Software',verbose_name=u'系统类型',blank=True,null=True)
    admin = models.ForeignKey(UserProfile,verbose_name='项目管理员',blank=True,null=True)

    # os_distribution = models.CharField(u'发型版本',max_length=64,blank=True,null=True)
    # os_release = models.CharField(u'操作系统版本',max_length=64,blank=True,null=True)

    create_date = models.DateTimeField(blank=True,auto_now_add=True)
    update_date = models.DateTimeField(blank=True,null=True)
    class Meta:
        verbose_name = '服务器'
        verbose_name_plural = '服务器'

    def __str__(self):
        return '%s SN:%s' %(self.asset.name,self.IPS)


class NetworkDevice(models.Model):
    vlan_ip = models.GenericIPAddressField(u'VlanIP',blank=True,null=True)
    intranet_ip = models.GenericIPAddressField(u'内网IP',blank=True,null=True)
    sn = models.CharField(u'SN号',max_length=128,unique=True)
    manufactory = models.CharField(u'制造商',max_length=64,blank=True,null=True)
    model = models.CharField(u'型号',max_length=128,null=True,blank=True)
    firmware = models.ForeignKey('Software',blank=True,null=True)
    port_num = models.SmallIntegerField(u'端口个数',null=True,blank=True)
    device_detail = models.TextField(u'设置详细配置',null=True,blank=True)
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(blank=True,null=True)

    class Meta:
        verbose_name = '网络设备'
        verbose_name_plural = '网络设备'

class Software(models.Model):
    os_types_choice = (('linux','Linux'),
                       ('windows','Windows'),
                       ('network_firmware','Network Firmware'),
                       ('software','Software'),
                       )
    os_distribution_choices = (('windows','Windows'),
                               ('centos','CentOS'),
                               ('redhat','Redhat'),
                               ('esxi','ESXI')
                               )
    type = models.CharField(u'系统类型',choices=os_types_choice,default=u'Linux',max_length=128)
    distribution = models.CharField(u'类型',choices=os_distribution_choices,default=u'redhat',max_length=128)
    version = models.CharField(u'软件／系统版本',max_length=64)
    language_choices = (('cn',u'中文'),
                        ('en',u'英文')
                        )
    language = models.CharField(u'系统语言',choices=language_choices,max_length=128)

    class Meta:
        verbose_name = '软件／系统'
        verbose_name_plural = '软件／系统'

    def __str__(self):
        return self.version


class CPU(models.Model):
    cpu_model = models.CharField(u'CPU型号',max_length=128,blank=True,null=True)
    cpu_count = models.SmallIntegerField(u'物理CPU个数',blank=True,null=True)
    cpu_core_count = models.SmallIntegerField(u'CPU核数',blank=True,null=True)
    memo = models.TextField(u'备注',null=True,blank=True)
    creat_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(blank=True,null=True)
    class Meta:
        verbose_name = 'CPU部件'
        verbose_name_plural = 'CPU部件'
    def __str__(self):
        return ("%s,%s")%(self.cpu_model,self.cpu_core_count)

class RAM(models.Model):
    sn = models.CharField(u'SN号',max_length=128,blank=True,null=True)
    model = models.CharField(u'内存型号',max_length=128,blank=True,null=True)
    manufactory = models.CharField(u'制造商',max_length=64,blank=True,null=True)
    slot = models.CharField(u'插槽',max_length=64,blank=True,null=True)
    capacity = models.CharField(u'内存大小(GB)',max_length=64)
    memo = models.CharField(u'备注',max_length=128,blank=True,null=True)
    create_date = models.DateTimeField(blank=True,auto_now_add=True)
    update_date = models.DateTimeField(blank=True,null=True)
    def __str__(self):
        return '%s:%s:%s' %(self.manufactory,self.slot,self.capacity)
    class Meta:
        verbose_name = 'RAM'
        verbose_name_plural = 'RAM'
        #unique_together = ("asset","slot")
    auto_create_fields = ['sn','slot','model','capacity']

class Disk(models.Model):
    sn = models.CharField(u'SN号',max_length=128,blank=True,null=True)
    slot = models.CharField(u'插槽位',max_length=64,blank=True,null=True)
    manufactory = models.CharField(u'制造商',max_length=64,blank=True,null=True)
    model = models.CharField(u'磁盘型号',max_length=128,blank=True,null=True)
    capacity = models.FloatField(u'磁盘容量GB')
    disk_iface_choice = (('SATA','SATA'),
                         ('SAS','SAS'),
                         ('SCSI','SCSI'),
                         ('SSD','SSD'),
                         )
    iface_type = models.CharField(u'接口类型',max_length=64,choices=disk_iface_choice,default='SAS',blank=True,null=True)
    memo = models.TextField(u'备注',blank=True,null=True)
    create_date = models.DateTimeField(blank=True,auto_now_add=True)
    update_date = models.DateTimeField(blank=True,null=True)

    auto_create_fields = ['sn','slot','manufactory','model','capacity']
    class Meta:
        #unique_together = ("asset","slot")
        verbose_name = '硬盘'
        verbose_name_plural = '硬盘'
    def __str__(self):
        return 'solt:%s capacity:%s' %(self.slot,self.capacity)

class NIC(models.Model):
    name = models.CharField(u'网卡名',max_length=64,blank=True,null=True)
    sn = models.CharField(u'SN号',max_length=128,blank=True,null=True)
    model = models.CharField(u'网卡型号',max_length=128,blank=True,null=True)
    macaddress = models.CharField(u'MAC',max_length=64,blank=True,null=True)
    ipaddress = models.GenericIPAddressField(u'IP',blank=True,null=True)
    netmask = models.CharField(u'子网掩码',max_length=64,blank=True,null=True)
    gateway = models.CharField(u'网关',max_length=64,blank=True,null=True)
    bonding = models.CharField(u'bond',max_length=64,blank=True,null=True)
    memo = models.CharField(u'备注',max_length=128,blank=True,null=True)
    create_date = models.DateTimeField(blank=True,auto_now_add=True)
    update_date = models.DateTimeField(blank=True,null=True)

    def __str__(self):
        return '%s:%s' % (self.macaddress,self.ipaddress)
    class Meta:
        verbose_name = u'网卡'
        verbose_name_plural = u"网卡"
    auto_create_fields = ['name','sn','model','macaddress','ipaddress']

# class RaidAdaptor(models.Model):
#     asset = models.ForeignKey('Asset')
#     sn = models.CharField(u'SN号',max_length=128,blank=True,null=True)
#     slot = models.CharField(u'插口',max_length=64,)
#     model = models.CharField(u'型号',max_length=64,blank=True,null=True)
#     memo = models.TextField(u'备注',blank=True,null=True)
#     create_date = models.DateTimeField(blank=True,auto_now_add=True)
#     update_date = models.DateTimeField(blank=True,null=True)
#     def __str__(self):
#         return self.name
#     class Meta:
#         unique_together = ("asset","slot")

class Manufactory(models.Model):
    manufactory = models.CharField(u'厂商名称',max_length=64,unique=True)
    model = models.CharField(u'设备型号',max_length=63,blank=True,null=True)
    support_num = models.CharField(u'支持电话',max_length=30,blank=True)
    memo = models.CharField(u'备注',max_length=128,blank=True)
    def __str__(self):
        return ("%s,%s")% (self.manufactory,self.model)
    class Meta:
        verbose_name = '厂商'
        verbose_name_plural = '厂商'

class BusinessUnit(models.Model):
    parent_unit = models.ForeignKey('self',related_name='parent_level',blank=True,null=True)
    name = models.CharField(u'业务线',max_length=64,blank=True,null=True)
    name_type = models.CharField(u'业务子线路',max_length=64,blank=True,null=True)
    memo = models.CharField(u'备注',max_length=64,blank=True)
    def __str__(self):
        return ("%s,%s,%s")% (self.name,self.name_type,self.memo)
    class Meta:
        verbose_name = '业务线'
        verbose_name_plural = '业务线'

class Contract(models.Model):
    sn = models.CharField(u'合同号',max_length=128,unique=True)
    name = models.CharField(u'合同名称',max_length=64)
    memo = models.TextField(u'备注',blank=True,null=True)
    price = models.IntegerField(u'合同金额')
    datail = models.TextField(u'合同详细',blank=True,null=True)
    start_date = models.DateField(blank=True)
    end_date = models.DateField(blank=True)
    license_num = models.IntegerField(u'License数量',blank=True)
    create_date = models.DateField(auto_now_add=True)
    update_date = models.DateField(auto_now=True)
    class Meta:
        verbose_name = '合同'
        verbose_name_plural = '合同'
    def __str__(self):
        return self.name

class IDC(models.Model):
    name = models.CharField(u'机房名称',max_length=64,unique=True)
    memo = models.CharField(u'备注',max_length=128,blank=True,null=True)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = '机房'
        verbose_name_plural = '机房'

class Tag(models.Model):
    name = models.CharField('网卡名',max_length=32,unique=True)
    #creater = models.ForeignKey(NIC,verbose_name="IP")
    def __str__(self):
        return self.name

# class EventLog(models.Model):
#     name = models.CharField(u'事件名称',max_length=100)
#     event_type_choices = ((1,u'硬件变更'),
#                           (2,u'新增配件'),
#                           (3,u'设备下线'),
#                           (4,u'设备上线'),
#                           (5,u'定期维护'),
#                           (6,u'业务上线/更新/变更'),
#                           (7,u'其它'),
#                           )
#     event_type = models.SmallIntegerField(u'事件类型',choices=event_type_choices,default=u'硬件变更')
#     asset = models.ForeignKey('Asset')
#     component = models.CharField('事件子项',max_length=255,blank=True,null=True)
#     detail = models.TextField(u'事件详情')
#     date = models.DateTimeField(u'事件时间',auto_now_add=True)
#     username = models.CharField(u'事件变更人',blank=True,null=True,max_length=64)
#     memo = models.TextField(u'备注',blank=True,null=True)
#
#     def __str__(self):
#         return self.name
#     class Meta:
#         verbose_name = '事件记录'
#         verbose_name_plural = '事件记录'
#     def colored_event_type(self):
#         if self.event_type == 1:
#             cell_html = '<span style="background: orange;">%s</span>'
#         elif self.event_type == 2:
#             cell_html = '<span style="background: yellowgreen;">%s</span>'
#         else:
#             cell_html = '<span>%s</span>'
#         return cell_html % self.get_event_type_display()
#     colored_event_type.allow_tags = True
#     colored_event_type.short_description = u'事件类型'

class NewAssetApprovalZone(models.Model):
    sn = models.CharField(u'资产SN号',max_length=128,unique=True)
    asset_type_choices = (('server',u'服务器'),
                          ('switch',u'交换机'),
                          ('router',u'路由器'),
                          ('firewall',u'防火墙'),
                          ('storage',u'存储设备'),
                          ('NLB','负载均衡'),
                          ('wireless',u'无线AP'),
                          ('software',u'软件资产'),
                          ('others',u'其它类'),
                          )
    asset_type = models.CharField(choices=asset_type_choices,max_length=64,default=u'服务器')
    manufactory = models.CharField(max_length=64,blank=True,null=True)
    model = models.CharField(max_length=128,blank=True,null=True)
    ram_size = models.IntegerField(blank=True,null=True)
    cpu_model = models.CharField(max_length=128,blank=True,null=True)
    cpu_count = models.IntegerField(blank=True,null=True)
    cpu_core_count = models.IntegerField(blank=True,null=True)
    os_distribution = models.CharField(max_length=64,blank=True,null=True)
    os_type = models.CharField(max_length=64,blank=True,null=True)
    os_release = models.CharField(max_length=64,blank=True,null=True)
    data = models.TextField(u'资产数据')
    date = models.DateTimeField(u'汇报日期',auto_now_add=True)
    approved = models.BooleanField(u'已批准',default=False)
    approved_by = models.CharField(u'申批人',blank=True,null=True,max_length=64)
    approved_date = models.DateTimeField(u'批准日期',blank=True,null=True)
    def __str__(self):
        return self.sn
    class Meta:
        verbose_name = '新上线待批准资产'
        verbose_name_plural = '新上线待批准次产'