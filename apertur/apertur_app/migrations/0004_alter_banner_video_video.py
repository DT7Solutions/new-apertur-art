# Generated by Django 4.1.3 on 2022-11-23 06:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apertur_app', '0003_banner_video'),
    ]

    operations = [
        migrations.AlterField(
            model_name='banner_video',
            name='Video',
            field=models.FileField(upload_to='video/%y/'),
        ),
    ]