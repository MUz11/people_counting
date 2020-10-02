from django.db import models

# Create your models here.
class counting(models.Model):
    time = models.DateTimeField(auto_now_add=True)
    human_in = models.CharField(max_length=255)
    human_out = models.CharField(max_length=255)
    location = models.CharField(max_length=255)