# Generated by Django 3.0.6 on 2020-05-28 20:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('poster', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='poster',
            name='is_posted_on_tg',
            field=models.BooleanField(default=False, verbose_name='ce lien fut posté'),
        ),
    ]
