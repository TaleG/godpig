#!/usr/bin/env python
# -*- coding:utf-8 -*-
from django.forms import ModelForm
from projectpig import models

class ArticleModelForm(ModelForm):

    class Meta:
        model = models.Projectpig
        exclude = ()
#添加from样式
    def __init__(self,*args,**kwargs):
        super(ArticleModelForm,self).__init__(*args,**kwargs)
        for field_name in self.base_fields:
            field = self.base_fields[field_name]
            field.widget.attrs.update({'class': 'form-control'})
