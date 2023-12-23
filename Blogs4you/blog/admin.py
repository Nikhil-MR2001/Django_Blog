from django.contrib import admin
from django.utils.html import format_html

from .models import *


# Register your models here.

# created a custom class for configuration of Admin panel
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('image_tag', 'title', 'description', 'created')
    search_fields = ('title', )



admin.site.register(Category, CategoryAdmin)
admin.site.register(Post)