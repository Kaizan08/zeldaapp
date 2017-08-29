# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-22 17:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('botw', '0007_auto_20170822_1710'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='item',
            name='locations_found',
            field=models.CharField(blank=True, max_length=1024, null=True),
        ),
        migrations.AlterField(
            model_name='item',
            name='rupee_val',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]