from django.db import models
from django.contrib.auth.models import User

class Url(models.Model):
    sUrl=models.CharField('url锻炼',max_length=200,unique=True)
    fullUrl=models.CharField('完整url',max_length=200)
        
    def __str__(self):
        return self.sUrl


class Mony(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,default=None, null=True)
    monero = models.IntegerField('门罗币数量',default=0)
    bitcoin = models.IntegerField('比特币数量',default=20)