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
            name='FKAbstractInheritancePlugin',
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
            name='FKModel',
            fields=[
                ('primary_key', models.PositiveIntegerField(serialize=False, primary_key=True)),
                ('title', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='SimpleModel',
            fields=[
                ('primary_key', models.PositiveIntegerField(serialize=False, primary_key=True)),
                ('title', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='FKPlugin',
            fields=[
                ('fkmodel_ptr', models.OneToOneField(parent_link=True, auto_created=True, to='project.FKModel')),
                ('cmsplugin_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='cms.CMSPlugin')),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin', 'project.fkmodel'),
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
        migrations.AddField(
            model_name='fkmodel',
            name='fk',
            field=models.ForeignKey(to='cms.CMSPlugin'),
        ),
        migrations.AddField(
            model_name='fkabstractinheritanceplugin',
            name='fk',
            field=models.ForeignKey(related_name='abstract_fk_model', to='cms.CMSPlugin'),
        ),
    ]
