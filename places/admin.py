from django.contrib import admin

from .models import GeoJson, PlaceImage


class PlaceImageInline(admin.TabularInline):
    model = PlaceImage


@admin.register(GeoJson)
class GeoJsonAdmin(admin.ModelAdmin):
    inlines = [
        PlaceImageInline,
    ]


admin.site.register(PlaceImage)
