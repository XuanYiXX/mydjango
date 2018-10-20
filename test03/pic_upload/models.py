# -*- coding:UTF-8 -*-
from django.db import models
from datetime import date
from django.urls import reverse


class Picture(models.Model):
    title = models.CharField("标题",max_length=100,blank=True,default='')
    image = models.ImageField("图片",upload_to="mypictures",blank=True)
    style = models.CharField("类别",max_length=100,blank=True,default='')
    date=models.DateField(default=date.today)

    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('pic_upload:pic_detail',args=[str(self.id)])
