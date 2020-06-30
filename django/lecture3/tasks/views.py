from django.forms import Form, CharField, IntegerField
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

tasks = []

class NewTaskForm(Form):
    task = CharField(label="New Task")
    # priority = IntegerField(label="Priority", min_value=1,max_value=5)

# Create your views here.
def index(request):
    # create the empty list in this particular session
    if "tasks" not in request.session:
        request.session["tasks"] = []
    return render(request, "tasks/index.html", {
        "tasks" : request.session["tasks"]
    })

def add(request):
    if request.method == "POST":
        form = NewTaskForm(request.POST)
        if form.is_valid():
            task = form.cleaned_data["task"]
            request.session["tasks"] += [task]
            return HttpResponseRedirect(reverse("tasks:index"))
        else:
            return render(request, "tasks/add.html", {
                "form": form
            })
    return render(request, "tasks/add.html", {
        "form":NewTaskForm()
    })