# Generated by Django 3.1.2 on 2020-10-31 13:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0002_auto_20201031_1318'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='persons',
            name='sex',
        ),
    ]