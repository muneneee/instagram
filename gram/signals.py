# from django.contrib.auth.models import User
# from django.db.models.signals import post_save
# from django.dispatch import receiver
# from .models import Profile
# from django.contrib.auth import get_user_model



# @receiver(post_save,sender= User)
# def create_user_profile(sender, instance, created, **kwargs):
#     if created:
#         Profile.objects.create(user=instance)
#     #else:
#      #   Profile.objects.create(user=instance)
#       #  post_save.connect(create_user_profile, sender=User)

    

# @receiver(post_save, sender=User)
# def save_user_profile(sender, instance, **kwargs):
#     instance.profile.save()




# User = get_user_model()

# random_= User.objects.last()

# random_.profile.followers.all()

# random_.is_following.all()