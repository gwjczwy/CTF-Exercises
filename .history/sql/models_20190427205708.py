from django.db import models
from django.utils.timezone import now #当前时间

class Check(models.Model):
    checkId=models.CharField('验证码id',max_length=200,unique=True)
    checkValue=models.CharField('验证码值',max_length=200)
    checkDate=models.DateTimeField('创建时间', default=now)