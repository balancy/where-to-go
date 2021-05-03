from django.db import models
from tinymce.models import HTMLField


class GeoJson(models.Model):
    title = models.CharField(max_length=100)
    description_short = models.TextField(default='', blank=True)
    description_long = HTMLField()
    longitude = models.FloatField()
    latitude = models.FloatField()


class PlaceImage(models.Model):
    image = models.FileField(upload_to='.', null=True)
    geojson = models.ForeignKey(
        GeoJson,
        on_delete=models.CASCADE,
        related_name='images')
    my_order = models.PositiveIntegerField(default=0, blank=False, null=False)

    class Meta(object):
        ordering = ['my_order']

    def __str__(self):
        return f'{self.__class__.__name__}<{self.image}>'
