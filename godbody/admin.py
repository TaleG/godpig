from django.contrib import admin
from godbody import models

# Register your models here.

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user','name','my_mail','phone','qq')

admin.site.register(models.UserProfile,UserProfileAdmin)