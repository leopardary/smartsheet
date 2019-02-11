# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-05-27 17:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('staircase', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='chamber',
            name='descriptionFile',
            field=models.FileField(blank=True, null=True, upload_to=models.CharField(max_length=30)),
        ),
        migrations.AlterField(
            model_name='wafer',
            name='wafertype',
            field=models.CharField(choices=[('PT', 'Particle Grade Wafer'), ('LR', 'Low Res Particle Grade Wafer'), ('MC', 'Mechanical Grade Wafer'), ('ER', 'External Reclaimed Wafer'), ('IR', 'Internal Reclaimed Wafer')], default='Internal Reclaimed Wafer', max_length=20),
        ),
    ]