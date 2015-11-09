#-*- coding:utf-8 -*-
from django.db import models
from django.contrib import admin
# Create your models here.
class Book(models.Model):
    ISBN = models.PositiveIntegerField(primary_key=True,blank=True)
    Title = models.CharField(max_length=30)
    AulthorID = models.ForeignKey('Author',related_name='ID')
    Publisher = models.CharField(max_length=50)
    PublishDate = models.DateField(auto_now_add=True)
    Price = models.FloatField(max_length=10)
    def __unicode__(self):
    	return  u'%s'%(self.AulthorID) 
class Author(models.Model):
    AulthorID = models.PositiveIntegerField(primary_key=True)
    Name = models.CharField(max_length=30)
    Age = models.DateField(auto_now_add=True)
    Country = models.CharField(max_length=30)
    def __unicode__(self):
    	return u"<h4>作者编号：<strong>%s</strong>&nbsp;&nbsp;&nbsp;作者姓名：<strong>%s</strong></h4>  出生年月：<strong>%s</strong>&nbsp;&nbsp;&nbsp;作者国籍:<strong>%s<strong>"%(self.AulthorID,self.Name,self.Age,self.Country) 

