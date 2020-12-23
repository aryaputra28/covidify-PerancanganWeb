from django.shortcuts import render, redirect
from .models import Rumah_Sakit
from .forms import Form_RS
from django.core import serializers
from django.http import HttpResponse

def tambahRS(request):
    form = Form_RS() #data dari form
    if request.method == "POST":
        input_form = Form_RS(request.POST)
        if input_form.is_valid():
            data = input_form.cleaned_data #datanya masuk ke dict cleaned_data, karna pas di cek dia udah valid
            input_rs = Rumah_Sakit() #panggil class di models

            input_rs.provinsi = data['provinsi'] #buat key value, data itu nama dict nya
            input_rs.nama_rs = data['nama_rs']
            input_rs.alamat = data['alamat']
            input_rs.telepon = data['telepon']
            input_rs.website = data['website']

            input_rs.save()
            data_terbaru = Rumah_Sakit.objects.all()

            return redirect('/listRS')
    else:
        rs = Rumah_Sakit.objects.all()
        context = {'form':form,'rs':rs}
        return render(request, 'list_rs/tambah_rs.html', context)

def listRS(request):
    all_data = Rumah_Sakit.objects.all()
    return render(request, 'list_rs/list_rs.html', {'ListRs':all_data})

def api_rs(request):
    rs = Rumah_Sakit.objects.all()
    json_rs = serializers.serialize('json', rs)
    return HttpResponse(json_rs, content_type="text/json-comment-filtered")