from django.contrib import admin
from .models import Category, Tag, Neurotransmitter, Supplement, Producent, Shop
from .forms import CategoryForm, NeurotransmitterForm
from django.utils.html import format_html

models = [Tag, Supplement, Producent, Shop]
admin.site.register(models)


class CategoryAdmin(admin.ModelAdmin):
    form = CategoryForm
    # filter_horizontal = ('name',)
    list_display = ('name', 'colored_name')
    fieldsets = (
        (None, {
            'fields': ('name', 'color')
            }),
        )

    def colored_name(self, obj):
        return format_html(
            f'<span style="background-color: {obj.color}; color:#fff">color</span>'
        )


class NeurotransmitterAdmin(admin.ModelAdmin):
    form = NeurotransmitterForm
    list_display = ('name', 'colored_name')
    fieldsets = (
        (None, {
            'fields': ('name', 'color')
            }),
        )

    def colored_name(self, obj):
        return format_html(
            f'<span style="background-color: {obj.color}; color:#fff">color</span>'
        )

admin.site.register(Category, CategoryAdmin)
admin.site.register(Neurotransmitter, NeurotransmitterAdmin)
