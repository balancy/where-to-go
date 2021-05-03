from django.db import models
from tinymce.models import HTMLField


class Place(models.Model):
    title = models.CharField(max_length=100)
    description_short = models.TextField(blank=True)
    description_long = HTMLField(blank=True)
    longitude = models.FloatField()
    latitude = models.FloatField()

    def __str__(self):
        return f'{self.__class__.__name__}<{self.title}>'


class PlaceImage(models.Model):
    image = models.FileField(upload_to='.')
    geojson = models.ForeignKey(
        Place,
        on_delete=models.CASCADE,
        related_name='images')
    image_order = models.PositiveIntegerField(default=0, blank=True)

    class Meta(object):
        ordering = ['image_order']

    def __str__(self):
        return f'{self.__class__.__name__}<{self.image}>'
