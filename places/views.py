from django.shortcuts import get_object_or_404, render
from django.http import JsonResponse

from .models import Place


def serialize_geojson(geojson):
    return {
        "type": "Feature",
        "geometry": {
            "type": "Point",
            "coordinates": [geojson.longitude, geojson.latitude]
        },
        "properties": {
            "title": geojson.title,
            "detailsUrl": f"places/{geojson.id}"
        }
    }


def show_index(request):
    features = [serialize_geojson(place) for place in Place.objects.all()]

    context = {
        "type": "FeatureCollection",
        "features": features,
    }

    return render(request, "index.html", context={"places": context})


def show_place_detail(request, place_id):
    place = get_object_or_404(Place, id=place_id)

    context = {
        "title": place.title,
        "imgs": [elm.image.url for elm in place.images.all()],
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
