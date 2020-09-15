from django.urls import path, include
from rest_framework import routers

from comments.views import CommentViewSets

router = routers.DefaultRouter()
router.register('', CommentViewSets)

urlpatterns = [
    path('', include(router.urls))
]
