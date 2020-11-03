from django.contrib import admin


from .models import Scan, Kategori, Peserta, Jadwal, Status

admin.site.register(Kategori)
admin.site.register(Peserta)
admin.site.register(Jadwal)
admin.site.register(Status)


@admin.register(Scan)
class ScanAdmin(admin.ModelAdmin):
    list_display = ['peserta', 'scan_jam', 'tgl_scan', 'status_absen']
