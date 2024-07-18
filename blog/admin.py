from django.contrib import admin
from .models import Post



class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'slug')
    list_filter = ['date']
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}
    
    
# Register your models here.
admin.site.register(Post, PostAdmin)