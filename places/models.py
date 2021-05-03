from django.db import models
from tinymce.models import HTMLField


class Place(models.Model):
    title = models.CharField(max_length=100, verbose_name="Название")
    description_short = models.TextField(
        blank=True,
        verbose_name="Короткое название",
    )
    description_long = HTMLField(
        blank=True,
        verbose_name="Полное название",
    )
    longitude = models.FloatField(verbose_name="Долгота")
    latitude = models.FloatField(verbose_name="Широта")

    def __str__(self):
        return self.title


class PlaceImage(models.Model):
    image = models.ImageField(upload_to=".", verbose_name="Фото")
    place = models.ForeignKey(
        Place,
        on_delete=models.CASCADE,
        related_name="images",
        verbose_name="Место",
    )
    image_order = models.PositiveIntegerField(
        default=0,
        blank=True,
        verbose_name="Порядок фото",
    )

    class Meta(object):
        ordering = ["image_order"]

    def __str__(self):
        return f"{self.place.title}, фото {self.image.url}"
