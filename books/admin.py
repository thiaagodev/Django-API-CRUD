from django.contrib import admin
from books.models import Books

# Register your models here.

class Book(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_link = ('id', 'title')
    search_fields = ('id', 'title',)
    list_per_page = 10

admin.site.register(Books, Book)
