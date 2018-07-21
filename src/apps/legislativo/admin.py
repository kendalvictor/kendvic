from django.contrib import admin
from import_export.admin import ExportMixin

from .models import Status, Tittle, Chapter, Article, Laws, Questions, Answer


@admin.register(Questions)
class QuestionsAdmin(admin.ModelAdmin):
    list_display = ('id', 'text', 'user', 'law', 'approved', 'displeases',
                    'comments')
    list_filter = (
        ('user', admin.RelatedOnlyFieldListFilter),
        ('law', admin.RelatedOnlyFieldListFilter)
    )
    readonly_fields = ('id', 'text', 'user', 'law', 'approved', 'displeases',
                       'comments')
    search_fields = ('text', )


@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = ('id', 'text', 'user', 'law', 'approved', 'displeases',
                    'like')
    list_filter = (
        ('user', admin.RelatedOnlyFieldListFilter),
        ('law', admin.RelatedOnlyFieldListFilter),
        ('question', admin.RelatedOnlyFieldListFilter)
    )
    readonly_fields = ('id', 'text', 'user', 'law', 'approved', 'displeases',
                       'like')
    search_fields = ('text', )


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


@admin.register(Laws)
class LawsAdmin(admin.ModelAdmin):
    list_display = ('id', 'tittle', 'status', 'url_spanish', 'url_quechua',
                    'article', 'chapter', 'title_legis')
    search_fields = ('tittle',)
    list_editable = ('tittle', 'status')
    list_filter = (
        ('article', admin.RelatedOnlyFieldListFilter),
        ('chapter', admin.RelatedOnlyFieldListFilter),
        ('title_legis', admin.RelatedOnlyFieldListFilter),
    )
    readonly_fields = ('chapter', 'title_legis')

    fieldsets = (
        (None, {
            'fields': ['tittle', 'url_spanish', 'url_quechua', 'status']
        }),
        ('Relaciones', {
            'fields': ('article', 'chapter', 'title_legis')
        }),
    )

    def save_model(self, request, obj, form, change):
        """
        Given a model instance save it to the database.
        """
        if obj.article and obj.article.chapter:
            obj.chapter = obj.article.chapter

            if obj.article.chapter.title:
                obj.title_legis = obj.article.chapter.title
        obj.save()
