# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-24 14:38
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('botw', '0012_auto_20170824_1437'),
    ]

    operations = [
        migrations.RenameField(
            model_name='item',
            old_name='category_id',
            new_name='category',
        ),
        migrations.RenameField(
            model_name='quest',
            old_name='type_id',
            new_name='type',
        ),
        migrations.RenameField(
            model_name='userquest',
            old_name='quest_id',
            new_name='quest',
        ),
        migrations.RenameField(
            model_name='userquest',
            old_name='user_id',
            new_name='user',
        ),
    ]