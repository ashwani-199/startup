from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from business.common_modules.mainServices import MainService

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

    path('summernote/', include('django_summernote.urls')),

# ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
]
# urlpatterns += staticfiles_urlpatterns()

handler404 = MainService.error_404
handler500 = MainService.error_500
handler403 = MainService.error_403
handler400 = MainService.error_400

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += staticfiles_urlpatterns()
else:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)