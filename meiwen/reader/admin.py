from django.contrib import admin

# Register your models here.
from reader.models import Reader, ReaderAdditional

class AuthorAdmin(admin.ModelAdmin):
    pass
    
admin.site.register(Reader)
admin.site.register(ReaderAdditional)
