# Generated by Django 5.1.2 on 2024-12-02 18:21

import main_app.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_cityarea_advertisementcampaign_max_budget_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExternalSystem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('token', models.CharField(default=main_app.models.generate_token, max_length=40, unique=True)),
            ],
        ),
    ]