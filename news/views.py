from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response
# Create your views here.
from rest_framework.viewsets import ModelViewSet

from comments.serializers import CommentEdit
from news.models import New
from news.serializers import NewSerializerList, NewSerializerDetail, NewSerializerEdit


class NewViewSets(ModelViewSet):
    serializer_class = NewSerializerEdit
    queryset = New.objects.all()

    @action(detail=True, methods=['post'])
    def comment(self, request, *args, **kwargs):
        serializer = CommentEdit(data=request.data)
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
            instance.news_id = self.kwargs.get('pk')
            instance.save()

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = NewSerializerDetail(instance)
        return Response(serializer.data)

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = NewSerializerList(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = NewSerializerList(queryset, many=True)
        return Response(serializer.data)
