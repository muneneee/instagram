from django.db import models
from pyuploadcare.dj.models import ImageField



class Image(models.Model):
    Image = ImageField(blank = False, manual_crop="")
    name = models.CharField(max_length = 20)
    caption= models.TextField()
    profile = models.ForeignKey('Profile', on_delete=models.CASCADE)
    posted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Profile:
    profile_photo = ImageField(blank = True, manual_crop="")
    bio = models.TextField()


    def __str__(self):
        return self.bio
    