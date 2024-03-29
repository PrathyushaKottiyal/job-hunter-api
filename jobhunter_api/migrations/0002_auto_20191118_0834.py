# Generated by Django 2.2 on 2019-11-18 08:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobhunter_api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='experience',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='location_preference',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='resume',
            field=models.URLField(default='', max_length=255),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='skills',
            field=models.CharField(default='', max_length=255),
        ),
    ]
