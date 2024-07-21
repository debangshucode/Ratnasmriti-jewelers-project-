from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(Main_Category)
class Main_CategoryAdmin(admin.ModelAdmin):
    list_display = ['Name','id']

@admin.register(Sub_Category)
class Sub_CategoryAdmin(admin.ModelAdmin):
    list_display = ['Name','id']

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['id','Name','status','section']
    list_editable =['status','section']

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ['title','date']