# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Colour',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('col', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('language', models.CharField(max_length=15)),
                ('colour', models.ForeignKey(to='analyser.Colour')),
            ],
        ),
        migrations.CreateModel(
            name='sentence',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('stext', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='word',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('wtext', models.CharField(max_length=20)),
                ('lang', models.ForeignKey(to='analyser.Language')),
            ],
        ),
    ]
