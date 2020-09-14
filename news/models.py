from django.contrib.auth import get_user_model
from django.db import models
from easy_thumbnails.fields import ThumbnailerImageField

User = get_user_model()

TYPE_CHOICES = (
    ('a', "All"),
    ('s', "Sport"),
    ('t', "Technology"),
    ('p', "Politics"),
)


# Create your models here.
class New(models.Model):
    title = models.CharField(max_length=255)
    short_body = models.TextField(null=True)
    body = models.TextField()
    type = models.CharField(max_length=5, choices=TYPE_CHOICES, default='a')
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    image = ThumbnailerImageField(upload_to='images/%Y/%m/%d/', null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def get_comments(self):
        if self.comments.exists():
            return [instance.get_data() for instance in self.comments.all()]
        return None

    def __str__(self):
        return self.title

    def author(self):
        if self.owner:
            return self.owner.username
        return 'No author'

    def image_detail(self):
        if self.image:
            return self.image['detail'].url
        return None

    def image_blog(self):
        if self.image:
            return self.image['blog'].url
        return None
