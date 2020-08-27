from django.contrib import admin

# Register your models here.
from news.models import New


@admin.register(New)
class ImagesAdmin(admin.ModelAdmin):
    pass
