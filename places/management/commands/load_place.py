from django.core.management.base import BaseCommand
from os.path import split as os_split
from urllib.parse import urlsplit

from places.models import Place, PlaceImage

import requests


class Command(BaseCommand):
    help = 'Loads place from JSON file'

    def add_arguments(self, parser):
        parser.add_argument('json_file_url', type=str)

    @staticmethod
    def download_img_and_link_to_place(place, img_url):
        response_img = requests.get(img_url)
        response_img.raise_for_status()

        img_url_path = urlsplit(img_url)[2]
        filename = os_split(img_url_path)[1]
        with open(f'media/{filename}', 'wb') as f:
            f.write(response_img.content)

        place_image = PlaceImage(
            place=place,
        )
        place_image.image.name = filename
        place_image.save()

    def handle(self, *args, **options):
        link = options['json_file_url']
        response = requests.get(link)
        response.raise_for_status()

        json = response.json()

        place = Place(
            title=json['title'],
            description_short=json['description_short'],
            description_long=json['description_long'],
            longitude=json['coordinates']['lng'],
            latitude=json['coordinates']['lat'],
        )

        place.save()

        if imgs_urls := json['imgs']:
            for img_url in imgs_urls:
                self.download_img_and_link_to_place(place, img_url)

        self.stdout.write(
            self.style.SUCCESS(f'Successfully added GeoJson {place.title}')
        )