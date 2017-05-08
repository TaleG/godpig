from django.contrib import admin
from godbody.models import *

from pypro.models import announcement, project, channel_list, secu_list, planshows

#公告管理
class jwl_admin_announcement(admin.ModelAdmin):
    list_display = ('create_time','announ_title','context','exec_time','sign_name','remark')
    search_fields=('context','exec_time','remark','create_time')
    list_filter = ('create_time','exec_time')
admin.site.register(announcement,jwl_admin_announcement)

#项目管理
class jwl_admin_project(admin.ModelAdmin):
    def xmzt(self, obj):
        js = obj.pstatus
        if js is None or js=='':
            pass
        else:
            return sys_dd_item.objects.filter(dd_id='pstatus', dd_item=js).values('dd_item_name')[0]['dd_item_name']

    # def xmqs(self, obj):
    #     js = obj.psecur
    #     if js == 0 or js is None or js == '':
    #         pass
    #     else:
    #         return sys_dd_item.objects.filter(dd_id='user_company', dd_item=js).values('dd_item_name')[0]['dd_item_name']

    # def xmqd(self, obj):
    #     js = obj.pchannel
    #     if js == 0 or js is None or js == '':
    #         pass
    #     else:
    #         return sys_dd_item.objects.filter(dd_id='user_company', dd_item=js).values('dd_item_name')[0]['dd_item_name']
    # #上线
    def mutiupdate_sx(self,request,queryset):
        queryset.update(pstatus=3)
    mutiupdate_sx.short_description='批量修改状态为‘上线’'
    #暂停
    def mutiupdate_zt(self,request,queryset):
        queryset.update(pstatus=2)
    mutiupdate_zt.short_description='批量修改状态为‘暂停’'
    actions = ['mutiupdate_sx','mutiupdate_zt']
    radio_fields = {'pallot':admin.VERTICAL}
    xmzt.short_description = u'项目状态'
    #xmqs.short_description = u'券商'
    #xmqd.short_description = u'渠道'
    search_fields = ('pjira',)
    list_filter = ('pstatus',)
    list_display = ('pnum','pjira','pname','pallot','p_channel','p_secu','pmen','pdate','ponliedate','xmzt',)
admin.site.register(project,jwl_admin_project)

class jwl_admin_planshows(admin.ModelAdmin):
    list_display = ('pstype','pstime','pstitle','psinfo','psremark')
admin.site.register(planshows,jwl_admin_planshows)

class jwl_admin_channel_list(admin.ModelAdmin):
    list_display = ('id_for_cha','name_for_cha')
admin.site.register(channel_list,jwl_admin_channel_list)

class jwl_admin_secu_list(admin.ModelAdmin):
    list_display = ('id_for_com','name_for_com')
admin.site.register(secu_list,jwl_admin_secu_list)