# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-06-11 05:43
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0014_auto_20180610_2208'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='foodresponse',
            name='endtime',
        ),
    ]
