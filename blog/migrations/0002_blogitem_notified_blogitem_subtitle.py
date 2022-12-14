# Generated by Django 4.0.6 on 2022-08-01 08:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogitem',
            name='notified',
            field=models.BooleanField(default=False, verbose_name='Была ли рассылка о этом посте'),
        ),
        migrations.AddField(
            model_name='blogitem',
            name='subtitle',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
