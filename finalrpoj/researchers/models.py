from django.db import models
from django.contrib.auth.models import User
from django.shortcuts import reverse
from django.conf import settings
class profileModel(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    rating = models.IntegerField(default=0)
    aver = models.FloatField(default=0)
    count = models.IntegerField(default=0)
    mobile = models.CharField(max_length=10)
    selects = (('R','Researcher'),('S','Student'))
    select = models.CharField(max_length=1, choices=selects)

    def __str__(self):
        return self.user.username + " : " +self.select
            
    
    def get_absolute_url(self):
        return reverse('details',args=[str(self.id)])


class aboutResearch(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    subject = models.CharField(max_length =500)
    about = models.TextField()
# Create your models here.

class contact(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    email = models.EmailField()
    body = models.TextField()