from django.urls import path , include
from. import views
urlpatterns = [
    path('', views.Home, name='blog-home'),
    path('api/v1/', include('blog.api.v1.urls', namespace='api-v1')),
]