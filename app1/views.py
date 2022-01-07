from django.shortcuts import render

# Create your views here.
"""
Definition of views.
"""

from datetime import datetime
from django.shortcuts import render
from django.http import HttpRequest
from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, Dasdfghjjango!")
def solution(request):
    return HttpResponse("my name is navinS")
def account():
    PASS