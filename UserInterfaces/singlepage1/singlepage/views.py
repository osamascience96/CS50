from django.http.response import Http404, HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "singlepage/index.html")


texts = ["Prophet Ibrahim", "Prophet Ishaq", "Prophet Ismael", "Prophet Muhammad"]

def section(request, num):
    if 1<= num <= 4:
        return HttpResponse(texts[num - 1])
    else:
        raise Http404("No Such Section")