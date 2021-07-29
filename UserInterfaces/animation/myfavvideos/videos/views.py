from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
from django.http.response import Http404, HttpResponse
from django.core import serializers
from .models import Videos

# Create your views here
def index(request):
    return render(request, "home/index.html");

def GetVideos(request):
    # get the start and end of the index
    start = int(request.GET.get("start"))
    end = int(request.GET.get("end"))

    try:
        VideoList = Videos.objects.filter(id__range=[start, end])
        return HttpResponse(serializers.serialize('json', VideoList), content_type="application/json");
    except ObjectDoesNotExist:
        return Http404("No Videos Available")