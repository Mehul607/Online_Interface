# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('analyser', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='colour',
            name='hashcode',
            field=models.CharField(max_length=10, default='#FFF000'),
        ),
    ]
