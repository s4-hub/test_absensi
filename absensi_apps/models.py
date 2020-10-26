import datetime
from django.db import models
from django.core.validators import RegexValidator
from django.contrib.auth.models import User

from akun.models import Profil

Validator = RegexValidator(
    regex='^[0-9]*$', message='Hanya Angka', code='NIK tidak valid')


class Kategori(models.Model):
    nama_kategori = models.CharField(max_length=30)
    jam_masuk = models.DateTimeField()
    jam_keluar = models.DateTimeField()

    def batas_jam(self):
        return self.jam_masuk + datetime.timedelta(minutes=5)


class Peserta(models.Model):
    user = models.ForeignKey(Profil, on_delete=models.CASCADE)

    kategori_peserta = models.ForeignKey(Kategori, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.nama


class Scan(models.Model):
    # access_token = models.CharField(max_length=100)
    peserta = models.ForeignKey(Peserta, on_delete=models.CASCADE)
    scan_jam = models.DateTimeField(auto_now_add=True)

    def status(self):
        qs = Kategori.objects.all()
        for a in qs:
            if self.scan_jam.time() < a.jam_masuk.time():
                return 'JAM MASUK'
            elif self.scan_jam.time() > a.jam_keluar.time():
                return 'JAM KELUAR'
            else:
                return 'INVALID'

    # def status(self):
    #     if self.scan_jam < Kategori.jam_masuk:
    #         print(scan_jam)
    #         return 'JAM MASUK'
    #     elif self.scan_jam > Kategori.jam_keluar:
    #         return 'JAM PULANG'
    #     else:
    #         return 'Invalid'

    # def __str__(self):
    #     return self.peserta.nama
