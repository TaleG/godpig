from django.contrib import admin
from django.contrib.admin import AdminSite
import time
from django.utils.translation import gettext_lazy as _, gettext_lazy
# Register your models here.
from django.contrib.contenttypes.models import ContentType
from django.http import HttpResponseRedirect
from godbody.models import UserProfile
from godbody.models import sys_dd_item, schedule, check_day, restdays


#字典管理
class jwl_admin_sys_dd_item(admin.ModelAdmin):
    list_display = ('dd_id', 'dd_item', 'dd_item_name')
    search_fields = ('dd_id', 'dd_item', 'dd_item_name')
    list_filter = ('dd_id', )
admin.site.register(sys_dd_item,jwl_admin_sys_dd_item)

#签到管理
class jwl_admin_check_day(admin.ModelAdmin):
    def get_account_state(self, obj):
        qd_time = time.strptime(str(obj.checkin_time),'%Y-%m-%d %H:%M:%S')

        if qd_time[3]>10:
            return u'<span style="color:red;font-weight:bold">%s</span>' % (u"迟到",)
        else:
            return u'<span style="color:green;font-weight:bold">%s</span>' % (u"正常",)

    get_account_state.short_description = u'签到状态'
    get_account_state.allow_tags = True
    list_display = ('check_name','check_date','checkin_time','checkout_time','get_account_state')
    search_fields=('check_name','check_date','checkin_time','checkout_time')
    list_filter = ('check_date',)

admin.site.register(check_day,jwl_admin_check_day)


#用户管理
class jwl_admin_user(admin.ModelAdmin):

    # uid= sys_dd_item.objects.filter(dd_item_name='员工')
    # abc=user.objects.filter(user_role_id=uid)
    #queryset = user.objects.filter(user_role__dd_item_name='普通员工')

    # def yhjs(self, obj):
    #
    #     js = obj.user_role_id
    #     if js ==0 or js is None:
    #         pass
    #     else:
    #         return sys_dd_item.objects.filter(dd_id='user_role_id', dd_item=js).values('dd_item_name')[0]['dd_item_name']
    #
    # def yhdj(self, obj):
    #     js = obj.user_grade
    #     if js ==0 or js is None:
    #         pass
    #     else:
    #         return sys_dd_item.objects.filter(dd_id='user_grade', dd_item=js).values('dd_item_name')[0]['dd_item_name']
    # def yhlx(self, obj):
    #     js = obj.user_type
    #     if js ==0 or js is None:
    #         pass
    #     else:
    #         return sys_dd_item.objects.filter(dd_id='user_type', dd_item=js).values('dd_item_name')[0]['dd_item_name']
    # def yhzlx(self, obj):
    #     js = obj.user_group_role
    #     if js ==0 or js is None:
    #         pass
    #     else:
    #         return sys_dd_item.objects.filter(dd_id='user_group_role', dd_item=js).values('dd_item_name')[0]['dd_item_name']
    # def yhgs(self, obj):
    #     js = obj.user_company
    #     if js ==0 or js is None or js=='':
    #         pass
    #     else:
    #         return sys_dd_item.objects.filter(dd_id='user_company', dd_item=js).values('dd_item_name')[0]['dd_item_name']

    class ListFilter(admin.SimpleListFilter):
        # Human-readable title which will be displayed in the
        # right admin sidebar just above the filter options.
        title = _('用户类型')

        # Parameter for the filter that will be used in the URL query.
        parameter_name = 'user_parameter'

        def lookups(self, request, model_admin):
            """
      返回一个元组，第一个元素是送到url里边的参数值，第二个元素是本人定义的名字
            """
            return (
                ('in', _('公司员工')),
                ('out', _('外部人员')),
            )

        def queryset(self, request, queryset):
            """
            Returns the filtered queryset based on the value
            provided in the query string and retrievable via
            `self.value()`.
            """

            if self.value() == 'in':
                return queryset.filter(user_type=1)
            if self.value() == 'out':
                return queryset.filter(user_type=2)

    # yhgs.short_description = u'公司'
    # yhzlx.short_description= u'组类型'
    # yhlx.short_description = u'员工类型'
    # yhjs.short_description = u'员工角色'
    # yhdj.short_description = u'员工级别'
    # list_display=('name','yhjs','yhdj','yhlx','yhzlx','yhgs','user_email','remark',)
    list_display=('name','user_email','remark',)
    search_fields = ('user_code','name','yhgs')
    list_filter = (ListFilter,)
    ordering = ('user_type',)

    #prepopulated_fields = {"user_type": ("user_group",)}

    # def object_link(self, item):
    #     url = item.get_absolute_url()
    #     return u'<a href={url}>open</a>'.format(url=url)
    # object_link.short_description = 'View on site'
    # object_link.allow_tags = True
admin.site.register(UserProfile,jwl_admin_user)

#值班管理
class jwl_admin_schedule(admin.ModelAdmin):
    list_display = ('sys_year','month','day','date_flag','west_day','dule_group','remark',)
    search_fields = ('^sys_year','^remark')
    list_filter = ('month','remark','sys_year',)
    actions=['exports','export_selected_objects','export_mon_selected_objects']
    #fields = (('sys_year','month','day'),'west_day','date_flag','dule_group',)
    list_editable = ('remark',)
    fieldsets = (
        (None, {
            'fields': ('sys_year', 'month', 'day', 'date_flag')
        }),
        ('Advanced options', {
            'classes': ('collapse',),
            #wide
            'fields': ('west_day', 'dule_group','remark'),
        }),
    )
    ordering = ('sys_year',)
    def exports(self,request,queryset):
        row_updated=queryset.update(dule_group = 'B')
        if row_updated==1:
            message_bit = "1 story was"
        else:
            message_bit = "%s stories were" % row_updated
        self.message_user(request, "%s successfully marked as published." % message_bit)
    exports.short_description = "批量修改小组为B"

    def export_mon_selected_objects(self, request, queryset):
        selected = request.POST.getlist(admin.ACTION_CHECKBOX_NAME)
        ct = ContentType.objects.get_for_model(queryset.model)
        message_bit = '月度标准报表已导出成功，请前往查看'
        self.message_user(request, "%s" % message_bit)
        return HttpResponseRedirect("/index/export_m/ct=%s&ids=%s," % (ct.pk, ",".join(selected)))

    export_mon_selected_objects.short_description = "导出月度标准样式报表--A"
    def export_selected_objects(self, request, queryset):
        selected = request.POST.getlist(admin.ACTION_CHECKBOX_NAME)
        ct = ContentType.objects.get_for_model(queryset.model)
        message_bit = '普通标准报表已导出成功，请前往查看'
        self.message_user(request, "%s" % message_bit)
        return HttpResponseRedirect("/index/export/ct=%s&ids=%s," % (ct.pk, ",".join(selected)))
    export_selected_objects.short_description = "导出普通标准样式报表--B"
admin.site.register(schedule,jwl_admin_schedule)


#加班管理
class jwl_admin_restdays(admin.ModelAdmin):
    list_display = ('wdate','wrecordmen','wweek','wmen','wtimes','wcontent')
    search_fields = ('wdate','wweek','wrecordmen',)
admin.site.register(restdays,jwl_admin_restdays)





