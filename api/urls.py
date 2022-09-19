from django.urls import path,include
from rest_framework.routers import DefaultRouter

from .views import PostViewSet

app_name = 'api'

router = DefaultRouter()
router.register(r'blog', PostViewSet, basename='blog')

urlpatterns = [
    path('', include(router.urls)),
]
