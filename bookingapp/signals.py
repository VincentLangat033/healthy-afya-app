from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Doctor

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Doctor.objects.create(user=instance)
        print("Doctor Profile Created!")

# post_save.connect(create_profile, sender=User)

@receiver(post_save, sender=User)
def update_profile(sender, instance, created, **kwargs):
    if created == False:
        instance.doctor.save()

        print("Doctor Profile Updated!")

# post_save.connect(update_profile, sender=User)