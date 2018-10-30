# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations
from showtimes.cinemaworker import populate_db


def populate(apps, schema_editor):
    populate_db()


class Migration(migrations.Migration):

    dependencies = [
        ('showtimes', '0002_auto_20181023_1631'),
    ]

    operations = [
        migrations.RunPython(populate),
    ]
