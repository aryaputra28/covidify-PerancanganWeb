from django.shortcuts import render
from .models import Rapid
from .forms import FormRapid
from django.http import HttpResponseRedirect

# Create your views here.

def rapidTest(request):
    obj = Rapid.objects.all() 
    context = {'obj': obj}
    return render(request, 'rapidTest/rapidTest.html', context)

def form_Rapid(request):
    form = FormRapid(request.POST or None)
   
    if (form.is_valid() and request.method == 'POST'):
        form.save()       
        return HttpResponseRedirect('/rapidTest')

    context = {'form': form}
    
    return render(request, 'rapidTest/formRapid.html', context)


    