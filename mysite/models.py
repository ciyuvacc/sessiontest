#coding:utf8
from django.db import models

class User(models.Model):
    name = models.CharField(max_length=20,null=False)
    email = models.EmailField()
    password = models.CharField(max_length=20,null=False)
    enabled = models.BooleanField(default=False)

    def __unicode__(self):
        return self.name
