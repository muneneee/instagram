from django.db import models
from pyuploadcare.dj.models import ImageField
from django.contrib.auth.models import User
from django.utils import timezone



class Profile(models.Model):
    profile_photo = ImageField(blank = True, manual_crop="")
    bio = models.TextField()
    account = models.OneToOneField(User, on_delete=models.CASCADE)






    def __str__(self):
        return self.bio
    





class Image(models.Model):
    image = ImageField(blank = False, manual_crop="")
    name = models.CharField(max_length = 20)
    caption= models.TextField()
    profile = models.ForeignKey('Profile', on_delete=models.CASCADE)
    posted = timezone.now()
    account = models.ForeignKey(User, on_delete=models.CASCADE)



    def save_image(self):
        self.save()

    


    def __str__(self):
        return self.name


