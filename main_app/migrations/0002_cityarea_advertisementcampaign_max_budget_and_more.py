# Generated by Django 5.1.2 on 2024-12-02 17:28

import datetime
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CityArea',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('description', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='advertisementcampaign',
            name='max_budget',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AddField(
            model_name='advertisementcampaign',
            name='max_parallel_runs',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='advertisementcampaign',
            name='max_runnings',
            field=models.PositiveIntegerField(default=0, validators=[django.core.validators.MinValueValidator(1)]),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='advertisementcampaign',
            name='media_asset',
            field=models.FileField(default='', upload_to='media_assets/'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='advertisementcampaign',
            name='min_time_between_runs',
            field=models.DurationField(default=datetime.timedelta(seconds=3600)),
        ),
        migrations.AddField(
            model_name='advertisementcampaign',
            name='city_areas',
            field=models.ManyToManyField(to='main_app.cityarea'),
        ),
    ]
