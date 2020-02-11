from django.shortcuts import render
from django.views.generic import TemplateView
from django.core.serializers import serialize
from django.http import HttpResponse
from django import forms
from leaflet.forms.widgets import LeafletWidget

from .models import Event, Point, Line, Polygon

# Create your views here.
class HomePageView(TemplateView):
    template_name = 'index.html'

def get_polygons(request):
    polygons = serialize('geojson', Polygon.objects.all(),
          geometry_field='points',
          fields=('name','description'))
    return HttpResponse(polygons, content_type='json')

class EditForm(forms.ModelForm):
    class Meta:
        model = Polygon
        fields = ('name', 'description', 'points')
        widgets = {'geom': LeafletWidget()}
