from django.shortcuts import render
from .models import Rapid
from .forms import FormRapid
from django.http import HttpResponseRedirect, HttpResponse
from django.core import serializers

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

def api_rapid(request):
    rpd = Rapid.objects.all()
    json_rpd = serializers.serialize('json', rpd)
    return HttpResponse(json_rpd, content_type="text/json-comment-filtered")

    