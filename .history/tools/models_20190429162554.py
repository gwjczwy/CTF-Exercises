from django.db import models

class Url(models.Model):
    sUrl=models.CharField('url锻炼',max_length=200,unique=True)
    fullUrl=models.CharField('完整url',max_length=200)
        
    def __str__(self):
        return self.sUrl

