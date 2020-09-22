from django.contrib.auth import get_user_model
from rest_framework import serializers

User = get_user_model()


class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'avatar', 'get_avatar']
        extra_kwargs = {
            'avatar': {'write_only': True},
            'get_avatar': {'read_only': True}
        }
