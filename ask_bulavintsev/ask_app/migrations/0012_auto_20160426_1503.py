# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-04-26 15:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ask_app', '0011_auto_20160426_1428'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quetion',
            name='tags',
            field=models.ManyToManyField(related_name='questions', to='ask_app.Tag'),
        ),
    ]
