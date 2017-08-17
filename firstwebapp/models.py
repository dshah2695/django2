from django.db import models

class login(models.Model):
    Username=models.CharField(max_length=10)
    Password=models.TextField(max_length=8)
