from rest_framework import serializers

from news.models import New


class NewSerializerList(serializers.ModelSerializer):
    type = serializers.CharField(source='get_type_display')

    class Meta:
        model = New
        fields = ['id', 'title', 'type', 'body', 'author', 'image_blog', 'image_detail', 'created_at', 'updated_at']


class NewSerializerEdit(serializers.ModelSerializer):
    class Meta:
        model = New
        fields = ['id', 'title', 'type', 'short_body', 'body', 'image']


class NewSerializerDetail(serializers.ModelSerializer):
    type = serializers.CharField(source='get_type_display')

    class Meta:
        model = New
        fields = ['id', 'title', 'type', 'short_body', 'body', 'author', 'image', 'image_blog', 'image_detail',
                  'created_at',
                  'updated_at']
