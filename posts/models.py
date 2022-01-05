from django.db import models

# Create your models here.
class post(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='posts/images/')
    date = models.DateField(auto_now=False)