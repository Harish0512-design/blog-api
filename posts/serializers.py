from django.contrib.auth.models import User
from rest_framework.serializers import ModelSerializer

from posts.models import Post


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"


class PostSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = "__all__"
