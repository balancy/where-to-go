from django.shortcuts import render

from .models import GeoJson


def serialize_geojson(geojson):
    return {
        "type": "Feature",
        "geometry": {
            "type": "Point",
            "coordinates": [geojson.longitude, geojson.latitude]
        },
        "properties": {
            "title": geojson.title,
            "placeId": geojson.placeId,
            "detailsUrl": ""
        }
    }


def show_index(request):
    features = [serialize_geojson(geojson) for geojson in GeoJson.objects.all()]

    data = {
        "type": "FeatureCollection",
        "features": features,
    }

    return render(request, "index.html", context={"data": data})
