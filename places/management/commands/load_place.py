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

        PlaceImage.objects.filter(
            place=place,
            image=filename,
        ).get_or_create(
            place=place,
            image=filename,
        )

    def handle(self, *args, **options):
        link = options['json_file_url']
        response = requests.get(link)
        response.raise_for_status()

        new_place = response.json()

        place, created = Place.objects.filter(
            title=new_place['title'],
        ).get_or_create(
            title=new_place['title'],
            description_short=new_place['description_short'],
            description_long=new_place['description_long'],
            longitude=new_place['coordinates']['lng'],
            latitude=new_place['coordinates']['lat'],
        )

        if imgs_urls := new_place['imgs']:
            for img_url in imgs_urls:
                self.download_img_and_link_to_place(place, img_url)

        self.stdout.write(
            self.style.SUCCESS(f'Successfully added GeoJson {place.title}')
        )
