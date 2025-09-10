from django.contrib import admin
from .models import Blogpost


@admin.register(Blogpost)
class BlogpostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'is_published',)
    search_fields = ('title', 'description',)
    ordering = ('title',)
