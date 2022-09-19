from rest_framework import permissions
from rest_framework import viewsets

from .serializers import PostSerializer
from blog.models import Post

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
