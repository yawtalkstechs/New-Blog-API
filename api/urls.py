from django.urls import path,include
from rest_framework.routers import DefaultRouter

from .views import PostViewSet

app_name = 'api'

router = DefaultRouter()
router.register(r'blogs', PostViewSet, basename='blogs')

urlpatterns = [
    path('', include(router.urls)),
]
