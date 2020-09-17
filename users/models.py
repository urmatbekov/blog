from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _
from easy_thumbnails.fields import ThumbnailerImageField


# Create your models here.
def content_file_name(instance, filename):
    return '/'.join(['avatars', instance.username, filename])


class User(AbstractUser):
    email = models.EmailField(_('email address'), unique=True, blank=True)
    avatar = ThumbnailerImageField(upload_to=content_file_name, blank=True, null=True)

    def get_avatar(self):
        if self.avatar:
            return self.avatar['avatar'].url
        return None

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')
        db_table = 'auth_user'
