# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-25 18:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='administrator',
            name='phone_number',
            field=models.IntegerField(max_length=12),
        ),
    ]
