from django.contrib import admin
from django.utils.html import format_html
from django.utils.safestring import mark_safe

from adminsortable2.admin import SortableInlineAdminMixin

from .models import Place, PlaceImage


class PlaceImageInline(SortableInlineAdminMixin, admin.TabularInline):
    model = PlaceImage
    readonly_fields = ('image_tag',)

    def image_tag(self, instance):
        return format_html(
            '<img src="{}" style="height: 200px;"/>',
            mark_safe(instance.image.url),
        ) or mark_safe(
           '<span class="errors">Can\'t find an image.</span>'
        )


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    inlines = [
        PlaceImageInline,
    ]


@admin.register(PlaceImage)
class PlaceImageAdmin(admin.ModelAdmin):
    raw_id_fields = ("place",)
