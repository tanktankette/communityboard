# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-13 22:37
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('messageboard', '0002_auto_20170813_2234'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='board',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='posts', to='messageboard.Board'),
        ),
    ]