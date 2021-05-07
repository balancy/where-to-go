from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render

from .models import Place


def serialize_place(place):
    return {
        "type": "Feature",
        "geometry": {
            "type": "Point",
            "coordinates": [place.longitude, place.latitude]
        },
        "properties": {
            "title": place.title,
            "detailsUrl": place.id,
        }
    }


def show_index(request):
    features_geojson = [serialize_place(place) for place in Place.objects.all()]

    places_geojson = {
        "type": "FeatureCollection",
        "features": features_geojson,
    }

    return render(request, "index.html", context={"places": places_geojson})


def show_place_detail(request, place_id):
    place = get_object_or_404(Place, id=place_id)

    context = {
        "title": place.title,
        "imgs": [place_image.image.url for place_image in place.images.all()],
        "description_short": place.description_short,
        "description_long": place.description_long,
        "coordinates": {
            "lat": place.latitude,
            "lng": place.longitude,
        }
    }

    return JsonResponse(
        context,
        json_dumps_params={
            "ensure_ascii": False,
            "indent": 4,
        }
    )
