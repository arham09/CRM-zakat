# Generated by Django 2.0.1 on 2018-06-03 10:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('donatur', '0005_auto_20180603_1026'),
    ]

    operations = [
        migrations.CreateModel(
            name='Donasi',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total', models.DecimalField(blank=True, decimal_places=2, max_digits=10000000000, null=True)),
                ('donatur', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='donatur.Donatur')),
            ],
        ),
        migrations.CreateModel(
            name='JenisDonasi',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=100)),
                ('deskripsi', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='donasi',
            name='jenis',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='pembayaran.JenisDonasi'),
        ),
    ]