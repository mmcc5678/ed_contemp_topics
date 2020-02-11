from django.contrib.gis.db import models

# Create your models here.

class Point(models.Model):
    name = models.CharField(max_length=256)
    description = models.CharField(max_length=256)
    points = models.PointField(verbose_name="Points")
    def __str__(self):
        return self.name

class Line(models.Model):
    name = models.CharField(max_length=256)
    description = models.CharField(max_length=256)
    points = models.LineStringField(verbose_name="Lines")
    def __str__(self):
        return self.name

class Polygon(models.Model):
    name = models.CharField(max_length=256)
    description = models.CharField(max_length=256)
    points = models.PolygonField(verbose_name="Polygons")
    def __str__(self):
        return self.name

class Event(models.Model):
    name = models.CharField(max_length=256)
    locale = models.CharField(max_length=256)
    polygons = models.ForeignKey(Polygon, on_delete=models.CASCADE, blank=True, null=True)
    lines = models.ForeignKey(Line, on_delete=models.CASCADE, blank=True, null=True)
    points = models.ForeignKey(Point, on_delete=models.CASCADE, blank=True, null=True)
    dtg = models.DateTimeField()
    dtg_added = models.DateTimeField(auto_now_add=True)
    dtg_updated = models.DateTimeField(auto_now=True)
    relevant_subjects = models.CharField(max_length=256)
    def __str__(self):
        return self.name
