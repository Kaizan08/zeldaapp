# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-28 17:51
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('botw', '0013_auto_20170824_1438'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Group',
            new_name='Set',
        ),
        migrations.RenameField(
            model_name='quest',
            old_name='group',
            new_name='set',
        ),
    ]
