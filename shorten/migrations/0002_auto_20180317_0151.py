# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-03-17 01:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shorten', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='url',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
