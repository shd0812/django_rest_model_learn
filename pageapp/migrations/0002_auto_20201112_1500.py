# Generated by Django 3.1.2 on 2020-11-12 15:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pageapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='silk',
            name='price',
            field=models.CharField(max_length=10),
        ),
    ]
