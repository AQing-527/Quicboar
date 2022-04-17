from django.db import models
# Create your models here.
class User(models.Model):
    ''' User info'''
    name = models.CharField(max_length=128,default='',unique=True)
    mail = models.EmailField(unique=True)
    password = models.CharField(max_length=256)
    course_list = models.CharField(max_length=128,default='')
    creat_time = models.DateTimeField(auto_now_add=True)


class Course(models.Model):
    ''' Course info'''
    c_name = models.CharField(max_length=128,default='',unique=True)
    c_type = models.CharField(max_length=128, default='', unique=True)
    c_info = models.CharField(max_length=128, default='', unique=True)
    c_pic_url = models.CharField(max_length=128, default='', unique=True)
    c_tutor = models.CharField(max_length=128, default='', unique=True)
    c_price_b= models.CharField(max_length=128, default='', unique=True)
    c_price_n = models.CharField(max_length=128, default='', unique=True)

class Tutor(models.Model):
    ''' Tutor info'''
    t_name = models.CharField(max_length=128, default='', unique=True)
    t_type = models.CharField(max_length=128, default='', unique=True)
    t_info = models.CharField(max_length=128, default='', unique=True)
    t_pic_url = models.CharField(max_length=128, default='', unique=True)