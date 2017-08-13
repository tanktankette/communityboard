from django.contrib import admin
from .models import Board, Post


# class BoardAdmin(admin.ModelAdmin):
#     prepopulated_fields = {'slug': ('title',)}

admin.site.register(Board)
admin.site.register(Post)
