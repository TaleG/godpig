from django.contrib import admin
from godcmdb import models
# Register your models here.

class AssetAdmin(admin.ModelAdmin):
    list_display = ('asset_type','name','sn','production_test','model','model_position','management_ip','business_unit','admin','idc','memo','create_date','update_date')
class ServerAdmin(admin.ModelAdmin):
    list_display = ('asset','created_by','cpu_info','mem_info','disk_info')
class CpuAdmin(admin.ModelAdmin):
    list_display = ('asset','cpu_model','cpu_count','cpu_core_count','memo','creat_date','update_date')

admin.site.register(models.Asset,AssetAdmin)
admin.site.register(models.Contract)
admin.site.register(models.BusinessUnit)
admin.site.register(models.CPU,CpuAdmin)
# admin.site.register(models.EventLog)
admin.site.register(models.Disk)
admin.site.register(models.Manufactory)
# admin.site.register(models.NIC)
admin.site.register(models.Server,ServerAdmin)
admin.site.register(models.RAM)
admin.site.register(models.Tag)
admin.site.register(models.Software)
admin.site.register(models.NewAssetApprovalZone)
admin.site.register(models.NetworkDevice)
admin.site.register(models.IDC)