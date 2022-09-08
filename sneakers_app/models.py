from pyexpat import model
from django.db import models

# Create your models here.

class Brand(models.Model):
  name = models.CharField(max_length=255)

  def __str__(self):
    return self.name

class Sneaker(models.Model):
  name = models.CharField(max_length=255)
  brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
  description = models.TextField()
  color = models.CharField(max_length=255)
  size = models.CharField(max_length=10)
  purchase_year = models.IntegerField

  def __str__(self):
    return self.name

