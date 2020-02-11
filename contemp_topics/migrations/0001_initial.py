# Generated by Django 2.2.9 on 2020-02-07 20:36

import django.contrib.gis.db.models.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Line',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('description', models.CharField(max_length=256)),
                ('points', django.contrib.gis.db.models.fields.LineStringField(srid=4326, verbose_name='Points')),
            ],
        ),
        migrations.CreateModel(
            name='Point',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('description', models.CharField(max_length=256)),
                ('points', django.contrib.gis.db.models.fields.PointField(srid=4326, verbose_name='Points')),
            ],
        ),
        migrations.CreateModel(
            name='Polygon',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('description', models.CharField(max_length=256)),
                ('points', django.contrib.gis.db.models.fields.PolygonField(srid=4326, verbose_name='Points')),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('locale', models.CharField(max_length=256)),
                ('dtg', models.DateTimeField()),
                ('dtg_added', models.DateTimeField(auto_now_add=True)),
                ('dtg_updated', models.DateTimeField(auto_now=True)),
                ('relevant_subjects', models.CharField(max_length=256)),
                ('lines', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='contemp_topics.Line')),
                ('points', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='contemp_topics.Point')),
                ('polygons', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='contemp_topics.Polygon')),
            ],
        ),
    ]