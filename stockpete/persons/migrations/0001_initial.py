# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-23 05:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('ph_num', models.CharField(max_length=10)),
                ('address', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=20)),
                ('state', models.CharField(max_length=20)),
                ('zip_code', models.DecimalField(decimal_places=0, max_digits=6)),
                ('email', models.CharField(max_length=50)),
                ('rating', models.DecimalField(decimal_places=2, max_digits=4)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField(auto_created=True)),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('ph_num', models.CharField(max_length=10)),
                ('address', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=20)),
                ('state', models.CharField(max_length=20)),
                ('zip_code', models.DecimalField(decimal_places=0, max_digits=6)),
                ('ssn', models.CharField(max_length=20)),
                ('hourly_rate', models.DecimalField(decimal_places=2, max_digits=4)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
