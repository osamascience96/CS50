from django.core.exceptions import ObjectDoesNotExist
from django.http.response import Http404, HttpResponse, JsonResponse
from django.shortcuts import render
from django.core import serializers
from .models import Prophet 

# Create your views here.
def index(request):
    return render(request, "singlepage/index.html")

def section(request, num):
    # if the Prophet Object returns Model.Doesnotexists exception, we can control it 
    try:
        ProphetObject = Prophet.objects.filter(id=num);
        return HttpResponse(serializers.serialize('json', ProphetObject), content_type="application/json");
    except ObjectDoesNotExist:
        return Http404("Not Found")