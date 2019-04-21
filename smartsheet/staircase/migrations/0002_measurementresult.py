# Generated by Django 2.1.5 on 2019-04-21 22:15

from django.db import migrations, models
import django.db.models.deletion
import staircase.models.Measurements.MeasurementResult


class Migration(migrations.Migration):

    dependencies = [
        ('staircase', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MeasurementResult',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datetime', models.DateTimeField(auto_now_add=True)),
                ('rawDataFile', models.FileField(blank=True, null=True, upload_to=staircase.models.Measurements.MeasurementResult.add_raw_data_file)),
                ('startingSlot', models.IntegerField()),
                ('endingSlot', models.IntegerField()),
                ('foup', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='staircase.Foup')),
            ],
        ),
    ]