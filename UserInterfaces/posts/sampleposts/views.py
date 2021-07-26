from typing import Dict
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render
from . import models
from time import sleep
from django.http.response import Http404, HttpResponse
from django.core import serializers

# Create your views here.
def index(request):
    return render(request, 'mychat/index.html')

def GetUsers(request):
    # Get All the users
    UserList = models.User.objects.all()
    return HttpResponse(serializers.serialize('json', UserList), content_type="application/json")

def posts(request):
    # getting the start and end points
    start = int(request.GET.get("start"))
    end = int(request.GET.get("end"))

    try:
        # select the chatlist between the start and end id range from the chats, also selecting the foriegn key with it
        ChatList = models.Chat.objects.filter(id__range=[start, end])

        # artifically delay speed of response
        sleep(1)

        # return the response
        return HttpResponse(serializers.serialize('json', ChatList), content_type="application/json");
    except ObjectDoesNotExist:
        return Http404("No Chat Available")





