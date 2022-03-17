# Generated by Django 4.0.3 on 2022-03-17 18:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user_auth_api', '0003_alter_user_password_alter_user_username'),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100)),
                ('location', models.CharField(blank=True, max_length=100)),
                ('favoritegenre', models.CharField(blank=True, choices=[('pop', 'Pop'), ('rock', 'Rock'), ('techno', 'Techno'), ('hiphop', 'Hip-hop'), ('jazz', 'Jazz'), ('rap', 'Rap'), ('country', 'Country'), ('metal', 'Metal'), ('alternative', 'Alternative'), ('indie', 'Indie')], default='', max_length=100)),
                ('image', models.CharField(blank=True, max_length=100)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user_auth_api.user')),
            ],
        ),
    ]
