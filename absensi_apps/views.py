from django.shortcuts import render, redirect
from rest_framework import viewsets, serializers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth.decorators import login_required

from .models import Scan, Peserta
from akun.models import Profil
from .forms import ScanForm
from .serializers import ScanSerializer


@login_required
def list_absen(request):
    user = request.user

    datas = Scan.objects.filter(peserta__user__user=user)
    return render(request, 'absensi_apps/list.html', {'datas': datas})


@login_required
def scan_absen(request, *args, **kwargs):
    cuser = request.user
    # user_scan = Peserta.objects.get(user=request.user)
    if request.method == 'POST':
        form = ScanForm(request.POST or None)

        if form.is_valid():
            # form.cleaned_data['peserta'] = cuser
            post = form.save(commit=False)

            # post.peserta = request.POST.get('id_peserta')
            # print(post.peserta)
            # print(post, user_scan)
            post.save()

            return redirect('absensi:list')
    else:
        form = ScanForm()
    return render(request, 'absensi_apps/scan.html', {'form': form, 'cuser': cuser})


# class ScanViewSet(viewsets.ModelViewSet):

#     serializer_class = ScanSerializer

#     def get_queryset(self):
#         cuser = self.request.user
#         queryset = Scan.objects.filter(peserta__user=cuser)
#         # return super().get_queryset()
#         return queryset

@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'List': '/scan-list/',
        'Scan': '/scan/',
    }
    return Response(api_urls)


@api_view(['GET'])
def scanList(request):
    if request.user.is_superuser:
        scans = Scan.objects.all()
    else:
        scans = Scan.objects.filter(peserta__user__user=request.user)
    serializer = ScanSerializer(scans, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def scanDetail(request, pk):
    if request.user.is_superuser:
        scans = Scan.objects.get(id=pk)
    else:
        scans = Scan.objects.filter(
            peserta__user__user=request.user).get(id=pk)
    serializer = ScanSerializer(scans, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def scanCreate(request):
    serializer = ScanSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)
