from django.shortcuts import render,get_object_or_404, redirect
from django.http import HttpResponse, Http404, HttpResponseRedirect
import requests
import json
from .models import *
from .forms import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import LoginForm, SignUpForm
from django.contrib.auth import authenticate, login, logout 

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

def listFeedback(request):
    feedbacks = Feedback.objects.all()
    return render (request,'main/feedbackList.html',{'feedbacks':feedbacks})

def signUp(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)
            return HttpResponseRedirect('/login')

        else:
            for msg in form.error_messages:
                messages.error(request, 'Invalid entry')

    else:
        form = SignUpForm()

    context = {
        'form' : form
    }

    return render(request, "main/signup.html", context)
    
def login_view(request):
    return render(request, 'main/login.html')
def logout_view(request):
    return redirect