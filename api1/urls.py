from django.urls import path, include
from . import views


urlpatterns = [
    path("blogposts/", views.BlogPostListCreate.as_view(), name="blogpost-view-creste"),
    path("blogposts/<int:pk>/", views.BlogPostRetrieveUpdateDestory.as_view(), name="update"),
    path('api-auth/', include('dj_rest_auth.urls')),
]