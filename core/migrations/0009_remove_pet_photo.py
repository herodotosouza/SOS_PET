# Generated by Django 3.2 on 2021-04-28 04:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_auto_20210428_0128'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pet',
            name='photo',
        ),
    ]
