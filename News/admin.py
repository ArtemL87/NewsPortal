from django.contrib import admin
from .models import Author, Post, Category, User, Comment


admin.site.register(Author)
admin.site.register(Post)
admin.site.register(Category)
admin.site.register(User)
admin.site.register(Comment)


# Register your models here.
