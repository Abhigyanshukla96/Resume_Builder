from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserDetails(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_info")
    full_name = models.CharField(max_length=255, null=True, blank=True)
    address = models.CharField(max_length=255, null=True, blank=True)
    phone = models.CharField(max_length=255, null=True, blank=True)
    email = models.EmailField(max_length=255, null=True, blank=True)
    about_you = models.TextField(null=True, blank=True, default="")
    education = models.TextField(null=True, blank=True, default="")
    career = models.TextField(null=True, blank=True, default="")
    job1_start = models.CharField(max_length=255, null=True, blank=True)
    job1_end = models.CharField(max_length=255, null=True, blank=True)
    job2_start = models.CharField(max_length=255, null=True, blank=True)
    job2_end = models.CharField(max_length=255, null=True, blank=True)
    job3_start = models.CharField(max_length=255, null=True, blank=True)
    job3_end=  models.CharField(max_length=255, null=True, blank=True)
    job1_details = models.TextField(default="")
    job2_details = models.TextField(default="")
    job3_details = models.TextField(default="")
    
    def __str__(self):
        return self.user
    