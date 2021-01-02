from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.http.response import HttpResponseRedirect
from main.models import Pengguna
from django.contrib.auth.models import User
from django.core import serializers
from django.http import HttpResponse

def forum(request):
    pertanyaan_form = pertanyaanForm(request.POST or None)
    objectPengguna = request.user
    listpertanyaan = pertanyaan.objects.all()
    context ={
                'pertanyaan':listpertanyaan,
                'pertanyaan_form':pertanyaan_form
            }
    if request.method == 'POST':
        if pertanyaan_form.is_valid():
            penggunaModel = Pengguna.objects.get(akun=objectPengguna)
            listpertanyaan.create(
                penanya = penggunaModel.namalengkap,
                location = penggunaModel.lokasi,
                pertanyaan = pertanyaan_form.cleaned_data.get('pertanyaan'),
                email = objectPengguna.email
            )
            return render(request,'forum.html',context)
    return render(request,'forum.html',context)
    

def lihatPertanyaan(request):
    listpertanyaan = pertanyaan.objects.all()
    pertanyaan_form = pertanyaanForm(request.POST or None)
    
    context = {
    'pertanyaan':listpertanyaan,
    'pertanyaan_form':pertanyaan_form
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
        'form_balasan' : balasan_form, 'count':b,'komenid':komen_id
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
            
def api_pertanyaan(request):
    question = pertanyaan.objects.all()
    json_question = serializers.serialize('json', question)
    return HttpResponse(json_question, content_type="text/json-comment-filtered")

def api_komen(request):
    comment = komentar.objects.all()
    json_comment = serializers.serialize('json', comment)
    return HttpResponse(json_comment, content_type="text/json-comment-filtereds")
    

