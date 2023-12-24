from django.contrib import admin
from . models import Quote


class QuoteAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'email', 'services', 'message', 'created_at', 'updated_at']

admin.site.register(Quote, QuoteAdmin)
