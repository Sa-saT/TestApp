from django.shortcuts import render
from rest_framework import generics, status
# from rest_framework.response import Response
# from .models import BlogPost
# from .serializers import BlogPostSerializer
# from rest_framework.views import APIView
from .serializers import CustomUserSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
# from django.conf import settings
from django.contrib.auth import get_user_model


# User = settings.AUTH_USER_MODEL
User = get_user_model()

class UserListView(generics.ListCreateAPIView):
    queryset = User.objects.all().order_by('-id')
    serializer_class = CustomUserSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = CustomUserSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

# class BlogPostListCreate(generics.ListCreateAPIView):
#     queryset = BlogPost.objects.all()
#     serializer_class = BlogPostSerializer

#     # List全てを削除できる機能
#     def delete(self, request, *args, **kwargs):
#         BlogPost.objects.all().delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

# class BlogPostRetrieveUpdateDestory(generics.RetrieveUpdateDestroyAPIView):
#     queryset = BlogPost.objects.all()
#     serializer_class = BlogPostSerializer
#     lookup_field = "pk"


# class BlogPostList(APIView):
#     def get(self, request, format=None):
#         # Get the title from the query parameters(if none, default to empty string)
#         title = request.query_params.get("title", "")

#         if title:
#             blog_posts = BlogPost.objects.filter(title__incontains=title)
#         else:
#             blog_posts = BlogPost.objects.all()

#         serializer = BlogPostSerializer(blog_posts, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)