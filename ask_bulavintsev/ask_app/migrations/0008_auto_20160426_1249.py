# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-04-26 12:49
from __future__ import unicode_literals

from django.db import migrations
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('ask_app', '0007_rating'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='quetion',
            managers=[
                ('manager', django.db.models.manager.Manager()),
            ],
        ),
    ]
