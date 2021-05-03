# Generated by Django 3.1.7 on 2021-03-23 16:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0004_placeimage'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='placeimage',
            name='path',
        ),
        migrations.AddField(
            model_name='placeimage',
            name='image',
            field=models.FileField(null=True, upload_to='media/'),
        ),
    ]