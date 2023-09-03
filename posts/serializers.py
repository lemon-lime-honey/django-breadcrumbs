from rest_framework import serializers
from .models import *


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'


class PostListSerializer(serializers.ModelField):
    class Meta:
        model = Post
        fields = '__all__'