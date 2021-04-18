from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
# Register your models here.
from .models import Post,Comment,Like
@admin.register(Post)
class ViewAdmin(ImportExportModelAdmin):
    list_display = ('content','image','liked','updated','created','author')
@admin.register(Comment)
class ViewAdmin(ImportExportModelAdmin):
    list_display = ('user','post','body','updated','created')
@admin.register(Like)
class ViewAdmin(ImportExportModelAdmin):
    list_display = ('user','post','value','updated','created')

