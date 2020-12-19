from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.http.response import HttpResponseRedirect
from main.models import Pengguna
from django.contrib.auth.models import User

def forum(request):
    pertanyaan_form = pertanyaanForm(request.POST or None)
    objectPengguna = request.user
    listpertanyaan = pertanyaan.objects.all()
    if request.method == 'POST':
        if pertanyaan_form.is_valid():
            penggunaModel = Pengguna.objects.get(akun=objectPengguna)
            listpertanyaan.create(
                penanya = penggunaModel.namalengkap,
                location = penggunaModel.lokasi,
                pertanyaan = pertanyaan_form.cleaned_data.get('pertanyaan'),
                email = objectPengguna.email
            )
            
            context ={
                'status':1, 'pertanyaan':listpertanyaan
            }

            return render(request,'forum.html',context)

    context ={
            'page_title':'Forum Keluarga',
            'pertanyaan_form':pertanyaan_form, 
            'status':2,
    }
    return render(request,'forum.html',context)
    

def lihatPertanyaan(request):
    listpertanyaan = pertanyaan.objects.all()
    
    context = {'page_title':'Forum Keluarga',
    'pertanyaan':listpertanyaan, 'status' :1
    }   

    return render(request,'forum.html',context)


def balas(request,komen_id):
    balasan = komentar.objects.all()
    listPertanyaan = pertanyaan.objects.get(id=komen_id)
    balasan_form = komenForm(request.POST or None)
    b=0
    for a in balasan :
        if a.tanya == listPertanyaan :
            b = b+1
    context = {
        'list_balasan' : balasan, 'pertanyaan':listPertanyaan,
        'form_balasan' : balasan_form, 'count':b
    }
    if request.method == 'POST' :
        objectPengguna = request.user
        penggunaModel = Pengguna.objects.get(akun=objectPengguna)
        if balasan_form.is_valid():
            balasan.create(
                pengomentar = penggunaModel.namalengkap,
                komen = balasan_form.cleaned_data.get('komen'),
                location =  penggunaModel.lokasi,
                tanya = listPertanyaan,
                email = objectPengguna.email
            )
            return redirect('qna:balas', komen_id=komen_id)
            
    return render(request,'forum-pertanyaan.html',context)
            
    

