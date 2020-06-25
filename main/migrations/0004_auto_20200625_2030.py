# Generated by Django 3.0.7 on 2020-06-25 14:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20200625_2015'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sensor',
            name='gas',
            field=models.FloatField(default=1, verbose_name='Gas'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='sensor',
            name='humidity',
            field=models.FloatField(default=1, verbose_name='Humidity'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='sensor',
            name='smoke',
            field=models.FloatField(default=1, verbose_name='Smoke'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='sensor',
            name='temperatura',
            field=models.FloatField(default=1, verbose_name='Temperatura'),
            preserve_default=False,
        ),
    ]