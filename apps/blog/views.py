from django.shortcuts import render , redirect
from django.contrib import messages
from . models import BlogPost, Category, Comment


def blog(request):
    """A view that displays a list of all the blog posts"""
    blog = BlogPost.objects.all().order_by('-id')
    recent_blog = BlogPost.objects.all().order_by('-id')[:3]
    category = Category.objects.all()
    
    context = {
        "blog_page": "active",
        "blog": blog,
        "recent_blog": recent_blog,
        "category": category
    }
    return render(request, 'blog/blog.html', context)

def blogDetail(request, id):
    blog_post = BlogPost.objects.get(id=id)
    recent_blog = BlogPost.objects.all().order_by('-id')[:3]
    category = Category.objects.all()
    comments = Comment.objects.all()

    context = {
        "detail_page": "active",
        "blog_post": blog_post,
        "recent_blog": recent_blog,
        "category": category,
        "comments": comments,
        "Total_comments": comments.count()
    }
    return render(request, 'blog/detail.html', context)


def commentsPost(request, id):
    if request.method == 'POST':
        blog = BlogPost.objects.get(id=id)
        name = request.POST['name']
        email = request.POST['email']
        website = request.POST['website']
        comments = request.POST['comments']

        Comment.objects.create(name=name, email=email, website_url=website, post_id=blog, content=comments)
        messages.success(request, 'Successfully Sent The Comments!')
        return redirect('blog')
    
    context = {"contact_page": "active"}
    return render(request, 'blog/detail.html', context)