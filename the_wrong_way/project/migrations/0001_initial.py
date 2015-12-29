# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0013_urlconfrevision'),
    ]

    operations = [
        migrations.CreateModel(
            name='SomeModel',
            fields=[
                ('primary_key', models.PositiveIntegerField(serialize=False, primary_key=True)),
            ],
        ),
        migrations.CreateModel(
            name='SomeCMSPlugin',
            fields=[
            ],
            options={
                'abstract': False,
            },
            bases=('project.somemodel', 'cms.cmsplugin'),
        ),
    ]
