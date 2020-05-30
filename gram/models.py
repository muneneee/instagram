from django.db import models
from pyuploadcare.dj.models import ImageField
from django.utils import timezone



class Profile:
    profile_photo = ImageField(blank = True, manual_crop="")
    bio = models.TextField()





    def __str__(self):
        return self.bio
    





class Image(models.Model):
    image = ImageField(blank = False, manual_crop="")
    name = models.CharField(max_length = 20)
    caption= models.TextField()
    #profile = models.ForeignKey('Profile', on_delete=models.CASCADE)
    posted = timezone.now()



    def save_image(self):
        self.save()

    


    def __str__(self):
        return self.name


