from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import Student

@receiver(post_save, sender=Student)
def create_user_for_student(sender, instance, created, **kwargs):
    if created and not instance.user:
        user = User.objects.create(username=f"{instance.first_name[0]}_{instance.last_name}@antay.kz")
        password = f"{instance.first_name}_{instance.last_name}"
        user.set_password(password) 
        user.save()
        instance.user = user
        instance.save()
