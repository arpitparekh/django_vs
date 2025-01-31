from django.db import models

# Create your models here.
class Product(models.Model):
  
  name = models.CharField(max_length=255)
  price = models.FloatField()
  quantity = models.IntegerField()
  description = models.TextField()

class Blog(models.Model):
  title = models.CharField(max_length=255)
  content = models.TextField()
  author = models.CharField(max_length=255)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  image = models.ImageField(upload_to='images/',blank=True,null=True)

  def __str__(self):
    return self.title

class Register(models.Model):
  pass
