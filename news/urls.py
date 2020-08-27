from django.urls import path, include
from rest_framework import routers

from news.views import NewViewSets

router = routers.DefaultRouter()
router.register('', NewViewSets)

urlpatterns = [
    path('', include(router.urls))
]
