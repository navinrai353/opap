"""
Definition of views.
"""

from datetime import datetime
from django.shortcuts import render
from django.http import HttpRequest
from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, Django!")
def solution(request):
    text="my name is navin rai"
    return HttpResponse(text)