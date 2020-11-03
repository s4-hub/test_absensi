from rest_framework import serializers

from .models import Scan


class ScanSerializer(serializers.ModelSerializer):
    peserta = serializers.StringRelatedField()

    class Meta:
        model = Scan
        fields = ('id', 'peserta',
                  'tgl_scan', 'scan_jam', 'status_absen')
