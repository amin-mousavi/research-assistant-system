from django.contrib import admin
from .models import Article, Comment

# Register your models here.

# class CommentInline(admin.StackedInline):
class CommentInline(admin.TabularInline):
    model = Comment
    # extra = 0    

class ArticleAdmin(admin.ModelAdmin):
    inlines = [
        CommentInline,
    ]
    search_fields = ['title', 'author',]
    
    list_filter = ('title',
                   'author',
                   'supervisor',
                   'supervisor_approve',
                   'head_of_department_approve',
                   'department_approve',
                   'deputy_of_education_approve'
    )






admin.site.register(Article, ArticleAdmin)
admin.site.register(Comment)