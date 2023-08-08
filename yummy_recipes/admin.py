from django.contrib import admin
from .models import Recipe, Comment
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Recipe)
class RecipeAdmin(SummernoteModelAdmin):

    """Allows admin to manage recipes via the admin panel"""
    list_display = ('name', 'slug', 'status', 'category', 'created_on')
    search_fields = ['name', 'description']
    list_filter = ('status', 'created_on', 'category')
    prepopulated_fields = {'slug': ('name',)}
    summernote_fields = ('description', 'ingredients', 'steps')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):

    """Allows admin to manage comments on recipes via the admin panel"""
    list_display = ('name', 'body', 'recipe', 'created_on', 'approved')
    list_filter = ('created_on', 'approved')
    search_fields = ('name', 'email', 'body')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(approved=True)
