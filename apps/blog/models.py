from django.db import models
from django.contrib.auth.models import User
from mptt.models import MPTTModel, TreeForeignKey



class Category(models.Model):
    title = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class BlogPost(models.Model):
    title = models.ForeignKey(Category, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    heading = models.CharField(max_length=100, null=True, blank=True)
    image = models.ImageField(upload_to='blog_post')
    paragraph = models.TextField()
    like = models.ManyToManyField(User, verbose_name='Post Likes', related_name='Likes')
    comment = models.ManyToManyField(User, verbose_name='Post Comments', related_name='Comments')
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.heading
    


class Like(models.Model):
    user_id = models.ForeignKey(User, verbose_name='User Id', related_name='User_Like',
                                on_delete=models.SET_NULL, null=True)
    post_id = models.ForeignKey(BlogPost, verbose_name='Post Id', related_name='Post_Like',
                                on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)


class Comment(MPTTModel):
    user_id = models.ForeignKey(User, related_name='User_Comment',
                                on_delete=models.SET_NULL, null=True)
    post_id = models.ForeignKey(BlogPost, related_name='Post_Comment',
                                on_delete=models.SET_NULL, null=True)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')
    name = models.CharField(max_length=100, null=True, blank=True)
    email = models.CharField(max_length=100, null=True, blank=True)
    website_url = models.CharField(max_length=100, null=True, blank=True)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class MPTTMeta:
        order_insertion_by = ['created_at']

    def __str__(self):
        return self.name
    