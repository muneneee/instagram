from django.db import models
from pyuploadcare.dj.models import ImageField
from django.contrib.auth.models import User
from django.utils import timezone



class Profile(models.Model):
    profile_photo = ImageField(blank = True, manual_crop="")
    bio = models.TextField()
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    followers = models.ManyToManyField(User, related_name='is_following', blank =True)
    #following = models.ManyToManyField(User, related_name='following', blank = True)



    def __str__(self):
        return f'{self.user.username} Profile'
    





class Image(models.Model):
    image = ImageField(blank = False, manual_crop="")
    name = models.CharField(max_length = 20)
    caption= models.TextField()
    posted = models.DateTimeField(auto_now_add=True)
    account = models.ForeignKey(User, on_delete=models.CASCADE, related_name='account')
    liked = models.ManyToManyField(User, default=None, blank = True, related_name='liked')


    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()

    @classmethod
    def update_image(cls, id ,name, caption):
        update = cls.objects.filter(id = id).update(name = name, caption=caption)
    


    @property
    def num_likes(self):
        return self.liked.all().count()

    


    def __str__(self):
        return self.name

LIKE_CHOICES = (
    ('Like', 'Like'),
    ('Unlike', 'Unlike'),
)


class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Image, on_delete=models.CASCADE)
    value = models.CharField(choices=LIKE_CHOICES, default='like', max_length =10)


    def __str__(self):
        return str(self.post)



class Comment(models.Model):
    post = models.ForeignKey('Image', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField(max_length=100)
    timestamp = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f'{self.user.username} Comment'
