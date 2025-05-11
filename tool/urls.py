from django.urls import path
from .views import *
from .image_convertor import *


urlpatterns = [

    path('<str:lng>/tool/<str:slug>', tool, name="tool"),
    path('convert/convert-file', convert, name="convert"),


]
