from django.db import models

# Create your models here.
class JenisDocument(models.Model):
    nama = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.nama

class Document(models.Model):
    nama = models.CharField(max_length=255, blank=True, null=True)
    jenis = models.ForeignKey(JenisDocument, on_delete=models.CASCADE, null=True)
    deskripsi = models.CharField(max_length=255, blank=True)
    total = models.DecimalField(max_digits=10000000000, null=True, blank=True, decimal_places=2)
    document = models.FileField(upload_to='documents/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nama

