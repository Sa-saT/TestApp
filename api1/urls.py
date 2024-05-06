from django.urls import path, re_path, include
from . import views
from django.contrib import admin
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView
    )
from django.views.generic import TemplateView, RedirectView
from djoser.views import TokenCreateView
from .views import UserListView

# from dj_rest_auth.views import LoginView
app_name = 'account'

urlpatterns = [
    # path('admin/', admin.site.urls),
    # path("blogposts/", views.BlogPostListCreate.as_view(), name="blogpost-view-creste"),
    # path("blogposts/<int:pk>/", views.BlogPostRetrieveUpdateDestory.as_view(), name="update"),
    # path('api-auth/', include('dj_rest_auth.urls')),
    # https://django-rest-framework-simplejwt.readthedocs.io/en/latest/getting_started.html#:~:text=Project-,Configuration,-Then%2C%20your%20django
    # トークンの取得
    path('api-auth/jwt/', TokenObtainPairView.as_view()),
    # トークンの再取得
    path('api-auth/jwt/refresh/', TokenRefreshView.as_view()),
    # path('api/jwt/login/', LoginView.as_view()),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='index.html')),
    re_path('', RedirectView.as_view(url='auth/')),
    # path('auth/token/login/', TokenCreateView.as_view(), name='token_create'),  # ログイン用のURL
    path('user-list-view/', UserListView.as_view()),
]