from django.contrib import admin

from .models import Post


class PostAdmin(admin.ModelAdmin):
    list_display = ["author", "created", "title"]


admin.site.register(Post, PostAdmin)
