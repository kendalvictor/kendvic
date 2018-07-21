from django.contrib import admin
from import_export.admin import ExportMixin

from .models import Status, Tittle, Chapter, Article, Laws


@admin.register(Status)
class StatusAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)
    list_editable = ('name', )


@admin.register(Tittle)
class TittleAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)
    list_editable = ('name', )


@admin.register(Chapter)
class ChapterAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'title')
    list_filter = ('title',)
    list_editable = ('name', 'title')


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'chapter')
    list_filter = ('chapter',)
    list_editable = ('name', 'chapter')