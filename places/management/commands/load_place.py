from django.core.management.base import BaseCommand

from places.models import Place, PlaceImage

import requests


class Command(BaseCommand):
    help = 'Loads place from JSON file'

    def add_arguments(self, parser):
        parser.add_argument('json_file_url', type=str)

    @staticmethod
    def link_img_to_place(geo_json, img_url):
        response_img = requests.get(img_url)
        response_img.raise_for_status()

        filename = img_url.split('/')[-1]
        with open(f'media/{filename}', 'wb') as f:
            f.write(response_img.content)

        place_image = PlaceImage(
            place=geo_json,
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
                self.link_img_to_place(place, img_url)

        self.stdout.write(
            self.style.SUCCESS(f'Successfully added GeoJson {place.title}')
        )