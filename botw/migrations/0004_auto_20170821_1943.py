# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-21 19:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('botw', '0003_auto_20170821_1938'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=1024),
        ),
        migrations.AlterField(
            model_name='item',
            name='locations_found',
            field=models.CharField(max_length=1024, null=True),
        ),
        migrations.AlterField(
            model_name='item',
            name='name',
            field=models.CharField(max_length=1024),
        ),
        migrations.AlterField(
            model_name='quest',
            name='quest_name',
            field=models.CharField(max_length=1024),
        ),
        migrations.AlterField(
            model_name='type',
            name='name',
            field=models.CharField(max_length=1024),
        ),
        migrations.AlterField(
            model_name='user',
            name='fname',
            field=models.CharField(max_length=1024),
        ),
        migrations.AlterField(
            model_name='user',
            name='hash',
            field=models.CharField(max_length=1024),
        ),
        migrations.AlterField(
            model_name='user',
            name='lname',
            field=models.CharField(max_length=1024),
        ),
        migrations.AlterField(
            model_name='user',
            name='salt',
            field=models.CharField(max_length=1024),
        ),
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(max_length=1024),
        ),
    ]
