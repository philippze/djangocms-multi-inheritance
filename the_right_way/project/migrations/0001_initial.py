# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0013_urlconfrevision'),
    ]

    operations = [
        migrations.CreateModel(
            name='AbstractInheritancePlugin',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='cms.CMSPlugin')),
                ('title', models.CharField(max_length=10)),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin', models.Model),
        ),
        migrations.CreateModel(
            name='IntermediatePluginClass',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='cms.CMSPlugin')),
                ('title', models.CharField(max_length=10)),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
        migrations.CreateModel(
            name='SimpleModel',
            fields=[
                ('primary_key', models.PositiveIntegerField(serialize=False, primary_key=True)),
                ('title', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='MultilevelInheritancePlugin',
            fields=[
                ('intermediatepluginclass_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='project.IntermediatePluginClass')),
            ],
            options={
                'abstract': False,
            },
            bases=('project.intermediatepluginclass',),
        ),
        migrations.CreateModel(
            name='SimpleInheritancePlugin',
            fields=[
                ('simplemodel_ptr', models.OneToOneField(parent_link=True, auto_created=True, to='project.SimpleModel')),
                ('cmsplugin_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='cms.CMSPlugin')),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin', 'project.simplemodel'),
        ),
    ]
