from django.contrib.gis import admin
from .models import Event, Point, Line, Polygon
from leaflet.admin import LeafletGeoAdmin

admin.site.register(Event, LeafletGeoAdmin)
admin.site.register(Point, LeafletGeoAdmin)
admin.site.register(Line, LeafletGeoAdmin)
admin.site.register(Polygon, LeafletGeoAdmin)
# Register your models here.
