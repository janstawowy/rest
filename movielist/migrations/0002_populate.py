# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations
from movielist.personworker import populate_db


def populate(apps, schema_editor):
    populate_db()


class Migration(migrations.Migration):

    dependencies = [
        ('movielist', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(populate),
    ]
