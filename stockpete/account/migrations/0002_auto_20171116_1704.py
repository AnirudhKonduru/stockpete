# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-16 17:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='portfolio',
            name='num',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
