from django.contrib import admin
from.models import Games, Category
from django.utils.safestring import mark_safe

class GamesAdmin(admin.ModelAdmin):
    list_display = ('id', 'category', 'title', 'content', 'created_at', 'get_photo', 'is_published')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'content')
    list_filter = ('is_published', 'id')
    list_editable = ['is_published', 'category']
    fields = ('title', 'content', 'photo', 'get_photo', 'is_published', 'created_at', 'updated_at')
    readonly_fields = ('get_photo', 'created_at', 'updated_at')

    def get_photo(self, obj):
        if obj.photo:
            return mark_safe(f'<img src="{obj.photo.url}" whidth="75">')
        else:
            return 'Фото нет'

    get_photo_description = 'Миниаутюра'
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')

admin.site.register(Games, GamesAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.site_title = 'Страница администратора'
admin.site.site_header = 'Страница администратора'

