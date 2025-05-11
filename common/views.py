from django.shortcuts import render
from .models import *
# Create your views here.


def get_header_footer():
    return {
        'header': Header.objects.all(),
        'footer': Footer.objects.all(),
    }