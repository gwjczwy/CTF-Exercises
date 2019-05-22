from django.db import models

class Check(models.Model):
    checkId=models.CharField('验证码id',max_length=200,unique=True)
    checkValue=models.CharField('验证码值',max_length=200)
    checkDate=models.IntegerField('创建时间')
        
    def __str__(self):
        return self.checkId
