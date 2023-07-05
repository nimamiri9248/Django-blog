from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("posts", views.PostViewSet, basename="posts")
router.register("categories", views.CategoryModelViewSet, basename="categories")
app_name = "api-v1"


# urlpatterns = [
#       # path('posts/', views.PostList.as_view(), name='post-list'),
#       # path('posts/<int:pk>/', views.PostDetail.as_view(), name='post-detail'),
#       path('posts/', views.PostViewSet.as_view({'get': 'list', 'post': 'create'}), name='post-list'),
#       path('posts/<int:pk>' , views.PostViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='post-detail'),
# ]
urlpatterns = router.urls
