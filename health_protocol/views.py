from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import *
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from main.models import Pengguna
from django.core.exceptions import *

# Create your views here.
def index(request):
    if request.method == "POST":

        form = AlternativesForm(request.POST)

        if form.is_valid():
            data = form.cleaned_data
            alternatives = Alternatives()
            preference = Preference()
            alternatives.pengguna = Pengguna.objects.get(akun=request.user)
            preference.pengguna = Pengguna.objects.get(akun=request.user)
            alternatives.text = data['text']
            alternatives.save()
            preference.alternatives = alternatives
            preference.save()
            messages.success(request, (f"Rekomendasi dari {request.user.username} berhasil ditambahkan!"))

            return redirect('health_protocol:healthProtocol')

    else:
        form = AlternativesForm()
        alternatives = Alternatives.objects.all()
        context = {
            'form': form,
            'alternatives': alternatives,
        }
        return render(request, 'health_protocol/index.html', context)

def alternatives(request):
    alternatives = Alternatives.objects.all()

    context = {
        'alternatives': alternatives,
    }
    
    return render(request, 'health_protocol/alternatives.html', context)

@login_required(login_url='main:login')
def alternativesPreference(request, alt_id, userpreference):
    if request.method == "POST":
        each_alt = get_object_or_404(Alternatives, id=alt_id)

        obj = ''
        valueobj = ''

        try:
            obj = Preference.objects.get(pengguna=request.user, alternatives=each_alt)
            valueobj = obj.value # value of userpreference
            valueobj = int(valueobj)
            userpreference = int(userpreference)

            if valueobj != userpreference:
                obj.delete()
                upref = Preference()
                upref.pengguna = request.user
                upref.alternatives = each_alt
                upref.value = userpreference

                if userpreference == 1 and valueobj != 1:
                    each_alt.upvotes += 1
                    each_alt.downvotes -= 1
                elif userpreference == 2 and valueobj != 2:
                    each_alt.downvotes += 1
                    each_alt.upvotes -= 1

                upref.save()

                each_alt.save()

                return redirect('health_protocol:alternatives')

            elif valueobj == userpreference:
                obj.delete()

                if userpreference == 1:
                    each_alt.upvotes -= 1
                elif userpreference == 2:
                    each_alt.downvotes -= 1

                each_alt.save()

                return redirect('health_protocol:alternatives')

        except Preference.DoesNotExist:
            upref = Preference()
            upref.pengguna = request.user
            upref.alternatives = each_alt
            upref.value = userpreference
            userpreference = int(userpreference)

            if userpreference == 1:
                each_alt.upvotes += 1
            elif userpreference == 2:
                each_alt.downvotes += 1

            upref.save()
            each_alt.save()

            return redirect('health_protocol:alternatives')

    else:
        each_alt = get_object_or_404(Alternatives, id=alt_id)

        return redirect('health_protocol:alternatives')
