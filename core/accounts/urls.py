from django.urls import path , include

urlpatterns = [
    path('v1/',include('accounts.v1.urls')),
    path("", include("djoser.urls")),
    path("", include("djoser.urls.jwt")),
]
