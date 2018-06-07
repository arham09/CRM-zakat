from django.db import models
from donatur.models import Donatur

# Create your models here.

class JenisDonasi(models.Model):
    nama = models.CharField(max_length=100)
    deskripsi = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.nama


class Donasi(models.Model):
    donatur     = models.ForeignKey(Donatur, on_delete=models.CASCADE)
    jenis       = models.ForeignKey(JenisDonasi, on_delete=models.CASCADE, null=True)
    total       = models.DecimalField(max_digits=10000000000, null=True, blank=True, decimal_places=2)
    date        = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.donatur.nama
