from django.contrib import admin
from .models import Book
 
class BookAdmin(admin.ModelAdmin):
      search_fields=['Name','Mobile']
      list_display=['Name']
   
admin.site.register(Book,BookAdmin)
