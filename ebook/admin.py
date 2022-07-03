from django.contrib import admin
from . models import EBooksModel 

# Register your models here.
@admin.register(EBooksModel)

class EBooksadmin(admin.ModelAdmin):
    pass

