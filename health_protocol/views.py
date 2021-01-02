from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import *
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from main.models import Pengguna
from django.core.exceptions import *
from django.http import JsonResponse

# Create your views here.
def index(request):
    if request.method == "POST":

        form = AlternativeForm(request.POST)

        if form.is_valid():
            data = form.cleaned_data
            alternatives = Alternative()
            alternatives.author = Pengguna.objects.get(akun=request.user)
            alternatives.text = data['text']
            alternatives.save()
            messages.success(request, (f"Rekomendasi dari {request.user.username} berhasil ditambahkan!"))

            return redirect('health_protocol:healthProtocol')

    else:
        form = AlternativeForm()
        alternatives = Alternative.objects.all()
        context = {
            'form': form,
            'alternatives': alternatives,
        }
        return render(request, 'health_protocol/index.html', context)

def alternatives(request):
    alternatives = Alternative.objects.all()

    if request.user.is_active:
        pengguna = Pengguna.objects.get(akun=request.user)

        context = {
            'alternatives': alternatives,
            'pengguna':pengguna,
        }

    else:
        context = {
            'alternatives': alternatives,
        }
    
    return render(request, 'health_protocol/alternatives.html', context)

@login_required(login_url='main:login')
def upvote(request):
    pengguna = Pengguna.objects.get(akun=request.user)
    if request.method == "POST":
        alternative_id = request.POST.get('alternative_id')
        alternatives = Alternative.objects.get(id=alternative_id)

        if pengguna in alternatives.liked.all():
            alternatives.liked.remove(pengguna)
        else:
            alternatives.liked.add(pengguna)

        upvote, created = Upvote.objects.get_or_create(pengguna=pengguna, alternatives_id=alternative_id)

        if not created:
            if upvote.value == 'Boleh tuh!':
                upvote.value = 'Skip deh...'
            else:
                upvote.value = 'Boleh tuh!'

        else:
            upvote.value = 'Boleh tuh!'

            alternatives.save()
            upvote.save()

        data = {
            'value':upvote.value,
            'upvotes':alternatives.liked.all().count(),
        }

        return JsonResponse(data, safe=True)

    return redirect('health_protocol:alternatives')
