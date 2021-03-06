# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-20 07:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='room',
            name='building',
        ),
        migrations.AlterField(
            model_name='singleresponse',
            name='room',
            field=models.IntegerField(default=100),
        ),
        migrations.AlterField(
            model_name='singleresponse',
            name='temp',
            field=models.IntegerField(choices=[(2, b'Very Hot!'), (1, b'Warm'), (0, b'Just right!'), (-1, b'Cool'), (-2, b'Very Cold!')], default=0),
        ),
        migrations.DeleteModel(
            name='Room',
        ),
    ]
