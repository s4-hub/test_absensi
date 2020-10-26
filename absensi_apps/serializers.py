from rest_framework import serializers

from .models import Scan


class ScanSerializer(serializers.ModelSerializer):
    # peserta = serializers.StringRelatedField(many=True)

    class Meta:
        model = Scan
        fields = ('peserta', 'scan_jam', 'status')
