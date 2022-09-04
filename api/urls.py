from django.urls import path
from .views import PostListView, PostDetailView

app_name = 'api'

urlpatterns = [
    path('blog/', PostListView.as_view()),
    path('blog/<int:pk>/', PostDetailView.as_view()),
]
