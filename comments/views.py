from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from comments.models import Comment
from comments.serializers import CommentEdit


class CommentViewSets(ModelViewSet):
    serializer_class = CommentEdit
    queryset = Comment.objects.all()

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.instance.get_data(), status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, serializer):
        request = self.request
        serializer.save()
        if request.user.id:
            instance = serializer.instance
            instance.owner = request.user
            instance.save()

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        if getattr(instance, '_prefetched_objects_cache', None):
            # If 'prefetch_related' has been applied to a queryset, we need to
            # forcibly invalidate the prefetch cache on the instance.
            instance._prefetched_objects_cache = {}

        return Response(serializer.inctance.get_data())

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        return Response(instance.get_data())
