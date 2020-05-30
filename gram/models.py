from django.db import models
from pyuploadcare.dj.models import ImageField



class Image(models.Model):
    Image = ImageField(blank = True, manual_crop="")
    name = models.CharField(max_length = 20)
    caption= models.TextField()
    
    