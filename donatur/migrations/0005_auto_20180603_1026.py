# Generated by Django 2.0.1 on 2018-06-03 10:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('donatur', '0004_auto_20180531_0625'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='donasi',
            name='donatur',
        ),
        migrations.RemoveField(
            model_name='donasi',
            name='jenis',
        ),
        migrations.DeleteModel(
            name='Donasi',
        ),
        migrations.DeleteModel(
            name='JenisDonasi',
        ),
    ]
