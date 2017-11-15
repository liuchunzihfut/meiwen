from django.contrib import admin

# Register your models here.
from book.models import Book, Content

class AuthorAdmin(admin.ModelAdmin):
    pass
    
admin.site.register(Book)
admin.site.register(Content)
