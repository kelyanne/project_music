# Generated by Django 3.0.3 on 2020-04-06 17:22

from django.db import migrations, models
import django.db.models.deletion
import stdimage.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Nome')),
            ],
            options={
                'verbose_name': 'Artista',
                'verbose_name_plural': 'Artistas',
            },
        ),
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Nome')),
                ('description', models.TextField(default=' ', max_length=200, verbose_name='Descrição')),
                ('image', stdimage.models.StdImageField(upload_to='album_images/', verbose_name='Imagem')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Criação')),
                ('artist', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='album', to='album.Artist')),
            ],
            options={
                'ordering': ['-created'],
            },
        ),
    ]
