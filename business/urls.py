"""
URL configuration for business project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


admin.site.site_title = "StartUp site admin"
admin.site.site_header = "StartUp Administration"
admin.site.index_title = "Site administration"

urlpatterns = [
    path('dashboard/', admin.site.urls),

    #apps include 
    path('', include('apps.home.urls')),
    path('about/', include('apps.about.urls')),
    path('services/', include('apps.services.urls')),
    path('blog/', include('apps.blog.urls')),
    path('contact/', include('apps.contact.urls')),
    path('features/', include('apps.features.urls')),
    path('price-plan/', include('apps.price_plan.urls')),
    path('quote/', include('apps.free_quote.urls')),
    path('team/', include('apps.team_members.urls')),
    path('testimonial/', include('apps.testimonial.urls')),
]
# ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += staticfiles_urlpatterns(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
