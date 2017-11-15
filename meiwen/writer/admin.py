from django.contrib import admin

# Register your models here.
from writer.models import Writer, Group

class AuthorAdmin(admin.ModelAdmin):
    pass
    
admin.site.register(Writer)
admin.site.register(Group)