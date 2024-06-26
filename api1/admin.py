from django.contrib import admin
from django.contrib.auth import get_user_model
# from django.contrib.auth.admin import UserAdmin
User = get_user_model()

class CustomUserAdmin(admin.ModelAdmin):
  model = User
  list_display = ['username', 'password']
  
admin.site.register(User)
# admin.site.register(CustomUserAdmin)