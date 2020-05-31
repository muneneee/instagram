from django.db import models
from pyuploadcare.dj.models import ImageField
from django.contrib.auth.models import User
from django.utils import timezone



class Profile(models.Model):
    profile_photo = ImageField(blank = True, manual_crop="")
    bio = models.TextField()
    user = models.OneToOneField(User, on_delete=models.CASCADE)




    def __str__(self):
        return f'{self.user.username} Profile'
    





class Image(models.Model):
    image = ImageField(blank = False, manual_crop="")
    name = models.CharField(max_length = 20)
    caption= models.TextField()
    posted = models.DateTimeField(default=timezone.now)
    account = models.ForeignKey(User, on_delete=models.CASCADE)



    def save_image(self):
        self.save()

    


    def __str__(self):
        return self.name


