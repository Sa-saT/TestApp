# API通信をする為、modelsのデータをJASONに変換する

from rest_framework import serializers
from .models import BlogPost
from django.contrib.auth import authenticate

class BlogPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogPost
        fields = ["id", "title", "content", "published_date"]

# cookie setting
# class LoginSerializer(serializers.Serializer):
#     """Login's Serializer"""
#     username = serializers.CharField(write_only=True)
#     password = serializers.CharField(write_only=True,style={'input_type': 'password'})

#     def validate(self, data):
#         username = data.get('username')
#         password = data.get('password')
#         if username and password:
#             user = authenticate(request=self.context.get('request'),
#                                 username=username,
#                                 password=password)
#             if user is None or not user.is_active:
#                 raise serializers.ValidationError("ログインが失敗しました")
#             data['user'] = user
#         return data