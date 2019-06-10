from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User, Post, Like

from .forms import SignUpForm

class UserAdmin(BaseUserAdmin):
    add_form = SignUpForm
    model = User
    list_display = ('email', 'is_staff', 'is_active',)
    list_filter = ('email', 'is_staff', 'is_active',)
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
    )
    search_fields = ('email',)
    ordering = ('email',)


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug','created_on')
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}

class LikeAdmin(admin.ModelAdmin):
    list_display = ('user', 'content_type','object_id', 'content_object')
    search_fields = ['user']

admin.site.register(Post, PostAdmin)
admin.site.register(User, UserAdmin)
admin.site.register(Like, LikeAdmin)
