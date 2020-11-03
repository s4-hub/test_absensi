from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator


Validator = RegexValidator(
    regex='^[0-9]*$', message='Hanya Angka', code='NIK tidak valid')


class Profil(models.Model):
    user = models.OneToOneField(User,
                                on_delete=models.CASCADE)
    nama = models.CharField(max_length=50)
    photo = models.ImageField(upload_to='users/%Y/%m/%d/',
                              blank=True)
    npk = models.CharField(max_length=9, validators=[Validator])

    def __str__(self):
        return self.nama
