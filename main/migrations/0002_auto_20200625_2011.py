# Generated by Django 3.0.7 on 2020-06-25 14:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sensor',
            name='gas',
            field=models.IntegerField(null=True, verbose_name='Gas'),
        ),
        migrations.AlterField(
            model_name='sensor',
            name='humidity',
            field=models.IntegerField(null=True, verbose_name='Humidity'),
        ),
        migrations.AlterField(
            model_name='sensor',
            name='smoke',
            field=models.IntegerField(null=True, verbose_name='Smoke'),
        ),
        migrations.AlterField(
            model_name='sensor',
            name='temperatura',
            field=models.IntegerField(null=True, verbose_name='Temperatura'),
        ),
    ]
