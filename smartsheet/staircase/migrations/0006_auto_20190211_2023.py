# Generated by Django 2.1.5 on 2019-02-12 04:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('staircase', '0005_auto_20190211_2004'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chamber',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='chamber',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
