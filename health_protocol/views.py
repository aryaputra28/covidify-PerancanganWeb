from django.shortcuts import render, redirect
from .models import *
from .forms import AlternativesForm
from django.contrib import messages

# Create your views here.
def index(request):
    if request.method == "POST":
        input_form = AlternativesForm(request.POST)
        if input_form.is_valid():

            data = input_form.cleaned_data

            input_alternatives = Alternatives()
            input_alternatives.username = data['username']
            input_alternatives.text = data['text']

            input_alternatives.save()
            messages.success(request, (f"Rekomendasi dari {request.POST['username']} berhasil ditambahkan!"))

            data_terbaru = Alternatives.objects.all()

            return redirect('health_protocol:healthProtocol')
    else:
        input_form = AlternativesForm()
        alternatives = Alternatives.objects.all()
        context = {
            'input_form':input_form,
            'alternatives':alternatives,
        }
        return render(request, 'health_protocol/index.html', context)

def alternatives(request):
    alternatives = Alternatives.objects.all()
    return render(request, 'health_protocol/alternatives.html', {'alternatives':alternatives})

def upvote(request, pk):
    alternatives = Alternatives.objects.get(id=pk)
    alternatives.upvotes += 1
    alternatives.save()
    return redirect('health_protocol:alternatives')

def downvote(request, pk):
    alternatives = Alternatives.objects.get(id=pk)
    alternatives.downvotes += 1
    alternatives.save()
    return redirect('health_protocol:alternatives')