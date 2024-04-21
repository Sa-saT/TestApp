from django.urls import path, include
from . import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView
    )
from dj_rest_auth.views import LoginView


urlpatterns = [
    path("blogposts/", views.BlogPostListCreate.as_view(), name="blogpost-view-creste"),
    path("blogposts/<int:pk>/", views.BlogPostRetrieveUpdateDestory.as_view(), name="update"),
    path('api-auth/', include('dj_rest_auth.urls')),
    # https://django-rest-framework-simplejwt.readthedocs.io/en/latest/getting_started.html#:~:text=Project-,Configuration,-Then%2C%20your%20django
    # トークンの取得
    path('api-auth/jwt/', TokenObtainPairView.as_view()),
    # トークンの再取得
    path('api-auth/jwt/refresh/', TokenRefreshView.as_view()),
    path('api/jwt/login/', LoginView.as_view()),
]