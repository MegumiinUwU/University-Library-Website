# Generated by Django 5.0.6 on 2024-05-20 21:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('default_pages', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='profile_picture',
            field=models.ImageField(blank=True, null=True, upload_to='profile_pictures/'),
        ),
    ]
