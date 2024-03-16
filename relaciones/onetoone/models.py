from django.db import models

# Create your models here.

class Place(models.Model):
  name = models.CharField(max_length=50)
  adress = models.CharField(max_length=80)

class Restaurant(models.Model):
  Place = models.OneToOneField(
    Place, on_delete = models.CASCADE, primary_key = True
  )
  employes =models.IntegerField(default=1)

   