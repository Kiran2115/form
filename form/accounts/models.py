from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

# Create your models here.
class Userprofile(models.Model):
    user =  models.OneToOneField(User)
    description = models.CharField(max_length = 100,default='')
    city = models.CharField(max_length = 100,default='')
    website = models.URLField(default='')
    phone = models.IntegerField(default =0)

def create_profile(sender,**kwargs):
    if kwargs['created']:
        user_profile = Userprofile.objects.create(user=kwargs['instance'])

post_save.connect(create_profile,sender=User)
