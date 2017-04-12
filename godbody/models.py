from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserProfile(models.Model):
    user = models.OneToOneField(User)
    name = models.CharField(u'名字',max_length=32)
    my_mail = models.CharField(u'邮箱',max_length=32)
    rank = models.CharField(u'级别',max_length=32)
    phone = models.CharField(u'电话',max_length=11)
    qq = models.CharField(u'QQ',max_length=16,blank=True,null=True)
    #signature = models.CharField(max_length=255,blank=True)
    #head_img = models.ImageField(height_field=150,width_field=150,blank=True,null=True)

    def __str__(self):
        return self.name