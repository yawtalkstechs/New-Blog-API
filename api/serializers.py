from rest_framework import serializers
from blog.models import Post

from taggit.serializers import TagListSerializerField, TaggitSerializer

class PostSerializer(TaggitSerializer, serializers.ModelSerializer):
    tags = TagListSerializerField()
    class Meta:
        model = Post
        # fields = '__all__'
        exclude = ['created', 'updated', 'slug']