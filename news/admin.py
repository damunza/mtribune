from django.contrib import admin
from .models import tags,Article

class ArticleAdmin(admin.ModelAdmin):
    filter_horizontal = ('tags',)

# Register your models here.
admin.site.register(tags)
admin.site.register(Article, ArticleAdmin)
