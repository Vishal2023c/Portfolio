from django.db import models

# Create your models here.
class contectEnquiry(models.Model):
    name=models.CharField(max_length=50)
    email=models.CharField(max_length=70)
    subject=models.CharField(max_length=70)
    message=models.TextField()