# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-21 19:38
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('botw', '0002_auto_20170821_1937'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Items',
            new_name='Item',
        ),
        migrations.RenameModel(
            old_name='ItemQuests',
            new_name='ItemQuest',
        ),
        migrations.RenameModel(
            old_name='Quests',
            new_name='Quest',
        ),
        migrations.RenameModel(
            old_name='UserQuests',
            new_name='UserQuest',
        ),
    ]
