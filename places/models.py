from django.db import models


class GeoJson(models.Model):
    title = models.CharField(max_length=100)
    description_short = models.TextField(null=True)
    description_long = models.TextField(null=True)
    longitude = models.FloatField()
    latitude = models.FloatField()

    def __str__(self):
        return f"{self.__class__.__name__}<{self.title}>"
