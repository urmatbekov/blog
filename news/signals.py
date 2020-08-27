from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver

from news.models import New

User = get_user_model()


@receiver(post_save, sender=New)
def create_user_profile(sender, instance, created, **kwargs):
    instance.objects.get_or_create(owner=instance)
