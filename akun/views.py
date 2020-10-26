from django.http import HttpResponse
from dal import autocomplete
from django.shortcuts import render, redirect
# from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from .models import Profil
from .forms import LoginForm, ProfilEditForm

@login_required
def dashboard(request):
    return render(request,
                  'account/dashboard.html',
                  {'section': 'dashboard'})


@login_required
def edit(request):
    if request.method == 'POST':
       
        profil_form = ProfilEditForm(
            instance=request.user.profile,
            data=request.POST,
            files=request.FILES)
        if profil_form.is_valid():
            
            profil_form.save()
            messages.success(request, 'Profile updated '
                             'successfully')
        else:
            messages.error(request, 'Error updating your profile')
    else:
       
        profil_form = ProfilEditForm(
            instance=request.user.profil)

    return render(request,
                  'account/edit.html',
                  {
                   'profil_form': profil_form})

@login_required
def input_profil(request):
    if request.method == 'POST':
        form = ProfilEditForm(request.POST)

        if form.is_valid():
            post = form.save(commit=False)
            # _,  created = Keluarga.objects.update_or_create(
            #     k_karyawan = 
            # )
            post.save()
            

            return redirect('hcp:tambah_k')
    else:
        form = ProfilEditForm()

    return render(request,'account/edit.html', {'form':form})

class AkunAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        if not self.request.user.is_authenticated:
            return User.objects.none()

        data_user = User.objects.all()
        
        if self.q:
            data_user = data_user.filter(username__icontains=self.q).order_by('id')
            
            # data_user = data_user.filter(full_name__icontains=self.q)
        return data_user 
