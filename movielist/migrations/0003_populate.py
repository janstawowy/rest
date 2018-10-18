# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations
from movielist.filmworker import populate_db


def populate(apps, schema_editor):
    populate_db()


class Migration(migrations.Migration):

    dependencies = [
        ('movielist', '0002_populate'),
    ]

    operations = [
        migrations.RunPython(populate),
    ]
