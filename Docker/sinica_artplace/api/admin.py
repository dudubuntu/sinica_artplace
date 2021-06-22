from django.contrib import admin
from django import forms
from ckeditor.widgets import CKEditorWidget

from .models import *


@admin.action(description='Опубликовать курсы')
def make_published(modeladmin, request, queryset):
    queryset.update(published=True)

@admin.action(description='Снять курсы с публикации')
def make_unpublished(modeladmin, request, queryset):
    queryset.update(published=False)


class ItemAdminForm(forms.ModelForm):
    description = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = Item
        fields = '__all__'


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('articul', 'name', 'price', 'published')
    list_filter = ('published', )
    list_display_links = ('articul', )
    list_editable = ('published', )
    list_ordering = ('articul', )
    search_fields = ('articul', 'name', 'author', 'description')
    readonly_fields = ('created', 'updated')
    actions = [make_published, make_unpublished]
    form = ItemAdminForm

    fieldsets = (
        ('general', {
            'fields': (('articul', 'name', 'author'), ('description',), 'event_date'),
            'classes': ('collapse',),
        }),
        ('images', {
            'fields': ('poster', 'author_img'),
            'classes': ('collapse',)
        }),
        ('price', {
            'fields': (('price',), ('action', 'previous_price')),
            'classes': ('collapse', )
        }),
        (None, {
            'fields': (('published', 'created', 'updated'),),
        })
    )


admin.site.register(Review)