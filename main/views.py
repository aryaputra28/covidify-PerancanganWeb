from django.shortcuts import render,get_object_or_404, redirect
from django.http import HttpResponse, Http404, HttpResponseRedirect
import requests
import json
from .models import *
from .forms import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

def home(request):
    url = "https://covid-193.p.rapidapi.com/statistics"
    querystring = {"country":"Indonesia"}
    headers = {
        'x-rapidapi-host': "covid-193.p.rapidapi.com",
        'x-rapidapi-key': "7b039c71a9msh11121f885beb4e5p15166bjsn0807437126b5"
        }
    response = requests.request("GET", url, headers=headers, params=querystring).json()
    data = response['response']
    d =data[0]
    # print(d)
    context = {
        'all' : d['cases']['total'],
        'recovered' : d['cases']['recovered']
    }
    return render(request, 'main/home.html',context)

def formFeedback(request):
    form = FeedbackForm()
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/feedbacks')
    context = {
        'form' : form,
    }
    return render(request, 'main/feedbackForm.html',context)
    
# @login_required(login_url="main:login")
def listFeedback(request):
    feedbacks = Feedback.objects.all()
    return render (request,'main/feedbackList.html',{'feedbacks':feedbacks})

def signUp(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        form2 = PenggunaForm(request.POST)
        userModel = Pengguna.objects.all()

        if form.is_valid() and form2.is_valid():
            user = form.save()
            userModel.create(
                namalengkap = form2.cleaned_data.get('namalengkap'),
                lokasi = form2.cleaned_data.get('lokasi'),
                institusi = form2.cleaned_data.get('institusi'),
                pekerjaan = form2.cleaned_data.get('pekerjaan'),
                akun = user
            )
            login(request, user)
            return HttpResponseRedirect('/')

        else:
            for msg in form.error_messages:
                messages.error(request, 'Invalid entry')

    else:
        form = SignUpForm()
        form2 = PenggunaForm()

    context = {
        'form' : form,
        'form2':form2,
    }

    return render(request, "main/signup.html", context)
    
def login_view(request):
    if request.method == 'POST':
        valuenext = request.POST.get('next')
        form = LoginForm(data = request.POST)

        if form.is_valid():
            usernameInput = request.POST["username"]
            passwordInput = request.POST["password"]

            user = authenticate(request, username=usernameInput, password=passwordInput)

            if user is not None and valuenext == "":
                login(request, user)
                return redirect('main:home')
            if user is not None and valuenext != "":
                login(request, user)
                return redirect(valuenext)
        else:
            messages.error(request, 'Invalid entry')

    else:
        form = LoginForm()

    context = {
        'form' : form,
    }

    return render(request, 'main/login.html', context)

@login_required
def logout_view(request):
    logout(request)
    form = LoginForm()
    response = {
        'form' : form,
    }
    return redirect('main:login')
