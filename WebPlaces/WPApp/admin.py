from django.contrib import admin
from .models import Category, Place, Comment, Favorite

admin.site.register(Category)
admin.site.register(Place)
admin.site.register(Comment)
admin.site.register(Favorite)
