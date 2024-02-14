from django.contrib import admin

# Register your models here.
from .models import article,comments
@admin.register(article)
class articleAdmin(admin.ModelAdmin):
    list_display=["title","author"]
    list_display_links=["title","author"]
    search_fields=["title"]
    list_filter=["datetime"]
    class Meta:
        model=article
@admin.register(comments)
class commentAdmin(admin.ModelAdmin):
    class Meta:
        model=comments   
    
