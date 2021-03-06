# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-01-28 02:02
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations
import django.db.models.deletion
import filer.fields.image


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.FILER_IMAGE_MODEL),
        ('geoslab', '0009_auto_20190127_1741'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='photos',
            field=filer.fields.image.FilerImageField(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='photos', to=settings.FILER_IMAGE_MODEL),
        ),
    ]
