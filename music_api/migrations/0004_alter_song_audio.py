# Generated by Django 4.0.3 on 2022-03-21 23:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music_api', '0003_alter_song_audio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='song',
            name='audio',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
