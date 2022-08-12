# Generated by Django 4.0.6 on 2022-08-12 11:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_token'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='subscribed',
            field=models.BooleanField(default=False, verbose_name='is user subscribed to blog'),
        ),
    ]