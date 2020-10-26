from django.contrib import admin


from .models import Scan, Kategori, Peserta

admin.site.register(Kategori)
admin.site.register(Peserta)

@admin.register(Scan)
class ScanAdmin(admin.ModelAdmin):
    list_display = ['peserta','scan_jam','status']
