from django.contrib import admin

# Register your models here.
from projectpig import models



class Projectpig(admin.ModelAdmin):
    list_display = ('project_name','person_in_charge','work_content','open_date','end_type')

class Project_speed(admin.ModelAdmin):
    list_display = ('article','project_track','end_type','name','Completion_date','expect_date')

class God_bug(admin.ModelAdmin):
    list_display = ('god_bug_date','god_bug_type','god_bug_ip','god_bug_phenomenon','god_bug_solve','god_bug_track','god_bug_registrant','god_bug_remarks')

class Bug_fault(admin.ModelAdmin):
    list_display = ('bug_code','bug_name','bug_version','bug_synopsis','bug_harm','bug_repair_work','bug_register_time','bug_registrant','memo')


admin.site.register(models.Projectpig,Projectpig)
admin.site.register(models.Project_speed,Project_speed)
admin.site.register(models.god_bug,God_bug)
admin.site.register(models.bug_fault,Bug_fault)
