# Generated by Django 2.1.5 on 2019-02-12 04:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('staircase', '0004_auto_20190210_2351'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chamber',
            name='timestamp',
            field=models.DateTimeField(editable=False),
        ),
        migrations.AlterField(
            model_name='chamber',
            name='updated',
            field=models.DateTimeField(),
        ),
    ]
