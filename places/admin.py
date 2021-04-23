from django.contrib import admin
from django.utils.html import format_html
from django.utils.safestring import mark_safe

from adminsortable2.admin import SortableAdminMixin, SortableInlineAdminMixin

from .models import GeoJson, PlaceImage


class PlaceImageInline(SortableInlineAdminMixin, admin.TabularInline):
    model = PlaceImage
    readonly_fields = ('image_tag',)

    def image_tag(self, instance):
        return format_html(
            f'<img src="{mark_safe(instance.image.url)}" style="height: 200px;"/>'
        ) or mark_safe(
            "<span class='errors'>Can't find an image.</span>"
        )


@admin.register(GeoJson)
class GeoJsonAdmin(admin.ModelAdmin):
    inlines = [
        PlaceImageInline,
    ]


admin.site.register(PlaceImage)
