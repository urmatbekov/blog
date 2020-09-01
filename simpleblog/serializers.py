from rest_framework import serializers

from news.models import New


class NewSerializerList(serializers.ModelSerializer):
    class Meta:
        model = New
        fields = ['id', 'title', 'type', 'body', 'author', 'image_blog', 'created_at', 'updated_at']


class NewSerializerEdit(serializers.ModelSerializer):
    class Meta:
        model = New
        fields = ['id', 'title', 'type', 'body', 'image', 'owner', 'created_at', 'updated_at']


class NewSerializerDetail(serializers.ModelSerializer):
    class Meta:
        model = New
        fields = ['id', 'title', 'type', 'body', 'author', 'image_detail', 'created_at', 'updated_at']
