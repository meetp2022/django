from django.db import models

# Create your models here.
class info(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=25)
    city = models.CharField(max_length=30)
    Comics = models.CharField(max_length=20)
