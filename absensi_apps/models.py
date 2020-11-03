import datetime
from django.db import models
from django.core.validators import RegexValidator
from django.contrib.auth.models import User

from akun.models import Profil

Validator = RegexValidator(
    regex='^[0-9]*$', message='Hanya Angka', code='NIK tidak valid')


class Kategori(models.Model):
    nama_kategori = models.CharField(max_length=30)
    # jam_masuk = models.DateTimeField()
    # jam_keluar = models.DateTimeField()

    # def batas_jam(self):
    #     return self.jam_masuk + datetime.timedelta(minutes=5)


class Jadwal(models.Model):
    kategori = models.ForeignKey(Kategori, on_delete=models.CASCADE)
    tgl_absen = models.DateField(auto_now_add=True)
    jam_masuk = models.TimeField()
    jam_pulang = models.TimeField()

    def batas_jam(self):
        return self.jam_masuk + datetime.timedelta(minutes=5)


class Peserta(models.Model):
    user = models.ForeignKey(Profil, on_delete=models.CASCADE)
    jadwal_peserta = models.ForeignKey(Jadwal, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.nama


class Status(models.Model):
    status = models.CharField(max_length=10)

    def __str__(self):
        return self.status


class Scan(models.Model):
    # access_token = models.CharField(max_length=100)
    peserta = models.ForeignKey(Peserta, on_delete=models.CASCADE)
    scan_jam = models.TimeField(auto_now_add=True)
    tgl_scan = models.DateField(auto_now_add=True)

    def status_absen(self):
        for qs in Jadwal.objects.all():
            if self.tgl_scan == qs.tgl_absen:

                if self.scan_jam < qs.jam_masuk:
                    return 'JAM MASUK'
                elif self.scan_jam > qs.jam_pulang and self.scan_jam < datetime.time(21, 0, 0):
                    return 'JAM PULANG'
                else:
                    return 'INVALID'

    # def jam_pulang(self):
    #     if self.scan_jam.date() == datetime.date.today():
    #         for qs in Jadwal.objects.all():
    #             if self.scan_jam.timetz() > qs.jam_masuk.timetz():
    #                 return self.scan_jam.astimezone().time()
    #     else:
    #         return 'None'

    # def save(self, *args, **kwargs):
    #     for a in Jadwal.objects.all():
    #         if self.scan_jam.date() == a.jam_masuk.date():
    #             # return self.scan_jam.astimezone().time()
    #             if self.scan_jam.time() < a.jam_masuk.time():
    #                 if (self.status_scan.status == 'JAM MASUK'):
    #                     self.status_scan.save(pk=3)
    #                     return super(Scan, self).save(*args, **kwargs)
    #                 else:
    #                     self.status_scan.save(pk=1)
    #                     return super(Scan, self).save(*args, **kwargs)
    #             elif self.scan_jam.time() > a.jam_pulang.time():
    #                 if self.jam_kegiatan() == 'JAM KELUAR':
    #                     return 'INVALID'
    #                 else:
    #                     return 'JAM KELUAR'
