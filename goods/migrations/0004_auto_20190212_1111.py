# Generated by Django 2.1.5 on 2019-02-12 03:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0003_auto_20171019_1219'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='address',
            name='user',
        ),
        migrations.RemoveField(
            model_name='orders',
            name='address',
        ),
        migrations.DeleteModel(
            name='Address',
        ),
    ]
