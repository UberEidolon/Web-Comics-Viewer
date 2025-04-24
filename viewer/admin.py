from django.contrib import admin

from .models import Manga, Page


class PageInline(admin.TabularInline):
    model = Page
    extra = 1

class MangaAdmin(admin.ModelAdmin):
    inlines = [PageInline]

admin.site.register(Manga, MangaAdmin)
