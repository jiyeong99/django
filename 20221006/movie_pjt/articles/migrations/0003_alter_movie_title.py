# Generated by Django 3.2.13 on 2022-10-06 09:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0002_alter_movie_running_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='title',
            field=models.TextField(),
        ),
    ]
