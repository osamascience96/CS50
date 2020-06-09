from .views import index, greet
from django.urls import path

urlpatterns = [
    # 1st args referes to nothing at the end of the file
    # 2nd args is the name of the function being called when this specific url is visited
    # 3rd args is the name given to this particular url, in order to be access from differnt parts of this application or other.
    path("", index, name="index"),
    path("<str:name>", greet, name="greet"),
]