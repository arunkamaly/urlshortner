from django.db import models
from django.contrib.auth.models import User


class urldetails(models.Model):
    fullurl = models.URLField()
    urlname = models.CharField(max_length=100, null=True)
    shorturl = models.CharField(max_length=100, unique=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    createdOn = models.DateTimeField(auto_now_add=True, null=True)
    updatedOn = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.urlname
    
    