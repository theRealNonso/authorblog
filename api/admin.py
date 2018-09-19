from django.contrib import admin
import api.models as am

# Register your models here


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('id', 'author', 'article', 'relaease_date')
    list_filter = ['relaease_date']
    search_fields = ['author']


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'username',
                    'bio', 'email')
    list_filter = ['username']
    search_fields = ['username']


admin.site.register(am.Articles, ArticleAdmin)
admin.site.register(am.Author, AuthorAdmin)
