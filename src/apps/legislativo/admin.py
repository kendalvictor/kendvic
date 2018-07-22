from django.contrib import admin
from import_export.admin import ExportMixin

from .models import Status, Tittle, Chapter, Article, Laws, Questions, Answer, Comision


@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = ('id', 'approved', 'text', 'user',  'question',
                    'displeases', 'like')
    list_filter = (
        ('user', admin.RelatedOnlyFieldListFilter),
        ('question', admin.RelatedOnlyFieldListFilter)
    )
    list_editable = ('approved', )
    readonly_fields = ('id',  'counter')
    search_fields = ('text', )

    def save_model(self, request, obj, form, change):
        """
        Given a model instance save it to the database.
        """

        if not obj.counter and obj.approved:
            if obj.question:
                obj.question.comments += 1
                obj.question.save()

            if obj.question and obj.question.law:
                obj.question.law.comments += 1
                obj.question.law.save()

            if obj.user:
                obj.user.comments += 1
                obj.user.save()

            obj.counter = True
        obj.save()


class AnswerInline(admin.TabularInline):
    model = Answer
    extra = 0
    readonly_fields = ('approved', 'counter')


@admin.register(Questions)
class QuestionsAdmin(admin.ModelAdmin):
    list_display = ('id', 'text', 'user', 'law', 'approved', 'displeases',
                    'comments')
    list_filter = (
        ('user', admin.RelatedOnlyFieldListFilter),
        ('law', admin.RelatedOnlyFieldListFilter)
    )
    readonly_fields = ('id', )
    search_fields = ('text', )
    inlines = [AnswerInline]


@admin.register(Status)
class StatusAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)
    list_editable = ('name', )


@admin.register(Comision)
class ComisionAdmin(admin.ModelAdmin):
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
    list_display = ('id', 'code', 'tittle', 'status', 'comision', 'published',
                    'url_spanish', 'url_quechua', 'article', 'chapter',
                    'title_legis', 'like', 'comments', 'views',
                    'displeases')
    search_fields = ('tittle', 'code')
    list_editable = ('published', 'tittle', 'status', 'comision', 'code',
                     'like', 'comments', 'views', 'displeases')
    list_filter = (
        ('article', admin.RelatedOnlyFieldListFilter),
        ('chapter', admin.RelatedOnlyFieldListFilter),
        ('title_legis', admin.RelatedOnlyFieldListFilter),
        ('comision', admin.RelatedOnlyFieldListFilter),
    )
    readonly_fields = ('chapter', 'title_legis')

    fieldsets = (
        (None, {
            'fields': ['code', 'tittle', 'url_spanish', 'url_quechua', 'status']
        }),
        ('Relaciones', {
            'fields': ('comision', 'article', 'chapter', 'title_legis')
        }),
        ('Conteos', {
            'fields': ('like', 'comments', 'views', 'displeases')
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
