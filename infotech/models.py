from django.db import models
class contact1(models.Model):
    name = models.CharField(max_length = 100)
    email = models.EmailField()
    mobileno = models.IntegerField(null = True)
    message = models.TextField()
# Create your models here.