# Generated by Django 2.0.1 on 2018-06-06 04:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('donatur', '0005_auto_20180603_1026'),
    ]

    operations = [
        migrations.AddField(
            model_name='donatur',
            name='institusi',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
