# Generated by Django 2.2.19 on 2021-02-28 13:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PIngueandoWebApp', '0003_auto_20210228_1043'),
    ]

    operations = [
        migrations.AddField(
            model_name='pinguer',
            name='active',
            field=models.BooleanField(default=False),
        ),
    ]
