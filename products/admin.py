from django.contrib import admin
from .models import *
from django.utils.safestring import mark_safe

@admin.register(Mens)
class AdminMen(admin.ModelAdmin):
    list_display = ['name','baha','description','photo'] 
    search_fields = ['name','description']
    list_filter = ['baha','name']
    list_display_links = ['name','baha']

    def photo(self, obj):
        return mark_safe(f'''
                <img src="{obj.image.url}" width="100"/>''')




@admin.register(Womens)
class AdminWomen(admin.ModelAdmin):
    list_display = ['name','baha','description','photo'] 
    search_fields = ['name','description']
    list_filter = ['baha','name']

    def photo(self, obj):
        return mark_safe(f'''
                <img src="{obj.image.url}" width="100"/>''')



    
@admin.register(Kids)
class AdminKid(admin.ModelAdmin):
    list_display = ['name','baha','description','photo'] 
    search_fields = ['name','description']
    list_filter = ['baha','name']

    def photo(self, obj):
        return mark_safe(f'''
                <img src="{obj.image.url}" width="100"/>''')


@admin.register(Accessories)
class AdminAccessories(admin.ModelAdmin):
    list_display = ['name','baha','description','photo'] 
    search_fields = ['name','description']
    list_filter = ['baha','name']

    def photo(self, obj):
        return mark_safe(f'''
                <img src="{obj.image.url}" width="100"/>''')