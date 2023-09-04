from django.contrib import admin
from .models import article, photo
from import_export.admin import ImportExportModelAdmin
from django.utils.html import format_html

class ArticleAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('title', 'date_created', 'date_updated')
    list_per_page = 1
    search_fields = ['title']
    prepopulated_fields = {'slug': ('title',)}

class PhotoAdmin(admin.ModelAdmin):
    def view(self, obj):
        return format_html('<img src="{}" style="max-width:200px; max-height:200px"/>'.format(obj.image.url))
    list_display = ['id', 'view',]

# Register your models here.
admin.site.register(article, ArticleAdmin)
admin.site.register(photo, PhotoAdmin)