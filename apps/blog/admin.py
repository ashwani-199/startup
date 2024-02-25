from django.contrib import admin
from . models import BlogPost, Category, Comment, Like
from mptt.admin import MPTTModelAdmin


class CustomMPTTModelAdmin(MPTTModelAdmin):
    list_display = ('id', 'post_id', 'parent', 'name', 'email', 'website_url', 'content', 'created_at')
    list_display_links = ('post_id',)
    mptt_level_indent = 20
admin.site.register(Comment, CustomMPTTModelAdmin)

class LikeAdmin(admin.ModelAdmin):
    list_display = ['id', 'user_id', 'post_id', 'created_at', 'updated_at']
admin.site.register(Like, LikeAdmin)

class BlogAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'user', 'heading', 'image', 'paragraph', 'created_at', 'updated_at']

admin.site.register(BlogPost, BlogAdmin)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'created_at', 'updated_at']
admin.site.register(Category, CategoryAdmin)
