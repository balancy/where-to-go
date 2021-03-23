from django.contrib import admin

from .models import GeoJson, PlaceImage

# Register your models here.
admin.site.register(GeoJson)
admin.site.register(PlaceImage)
