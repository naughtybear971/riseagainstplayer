# Generated by Django 2.2.5 on 2020-01-15 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('steam', '0029_gamescore'),
    ]

    operations = [
        migrations.AlterField(
            model_name='steam',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='game_pics'),
        ),
    ]
