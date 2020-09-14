from rest_framework import serializers

from comments.models import Comment


class CommentEdit(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'owner', 'body', 'news', 'parent', 'get_answers']
