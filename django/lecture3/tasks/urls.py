from django.urls import path

from .views import index, add

# the app name variable is the build in variable that helps us to avoid the namespace collision
app_name = "tasks"
urlpatterns = [
    path("", index, name="index"),
    path("add", add, name="add")
]