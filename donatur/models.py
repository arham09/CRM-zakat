from django.db import models

# Create your models here.
class Donatur(models.Model):
    nama    = models.CharField(max_length=100)
    email   = models.EmailField(null=True, blank=True)
    alamat  = models.CharField(max_length=100, null=True, blank=True)
    contact = models.CharField(max_length=100, null=True, blank=True)
    umur    = models.IntegerField()
    pekerjaan   = models.CharField(max_length=100, null=True, blank=True)
    institusi = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.nama


    