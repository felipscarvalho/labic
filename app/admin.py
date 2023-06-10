from django.contrib import admin
from django.db import models
from .models import Articles, ExtendUser, Projects
from markdownx.admin import MarkdownxModelAdmin
from django.contrib.auth.admin import UserAdmin
from markdownx.widgets import AdminMarkdownxWidget

# Register your models here.


class CustomUserAdmin(UserAdmin):
    fieldsets = (
        *UserAdmin.fieldsets,  # original form fieldsets, expanded
        (                      # new fieldset added on to the bottom
            # group heading of your choice; set to None for a blank space instead of a header
            'Aditional Info',
            {
                'fields': (
                    'profile_photo',
                    'user_level',
                    'description',
                ),
            },
        ),
    )


class CustomArticleAdmin(admin.ModelAdmin):
    search_fields = ['title']
    list_display = ['title', 'author',
                    'project', 'post_status', 'created_date']
    readonly_fields = ['created_date']
    formfield_overrides = {
        models.TextField: {'widget': AdminMarkdownxWidget},
    }
    fieldsets = [(
        'Heading',
        {
            'fields': [
                'cover',
                'title',
                'description',
                'author',
                'project',
                'post_status',
            ]
        },
    ),
        (
        'Post Body',
        {
            'fields': [
                'created_date',
                'markdownFile'
            ]
        }
    )]


class CustomProjectAdmin(admin.ModelAdmin):
    search_fields = ['title']
    list_display = ['title', 'author', 'project_status', 'created_date']
    readonly_fields = ['created_date']
    formfield_overrides = {
        models.TextField: {'widget': AdminMarkdownxWidget},
    }
    fieldsets = [(
        'Heading',
        {
            'fields': [
                'cover',
                'title',
                'description',
                'author',
                'project_status',
            ]
        },
    ),
        (
        'Post Body',
        {
            'fields': [
                'created_date',
                'markdownFile'
            ]
        }
    )]


admin.site.register(Articles, CustomArticleAdmin)
admin.site.register(Projects, CustomProjectAdmin)
admin.site.register(ExtendUser, CustomUserAdmin)
