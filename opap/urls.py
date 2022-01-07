"""
Definition of urls for opap.
"""

from datetime import datetime
from django.urls import path
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from app import forms, views
from django.conf.urls import include, url
import app1.views


urlpatterns = [
# Django processes URL patterns in the order they appear in the array
    url(r'^$', app1.views.index, name='index'),
    url(r'^home$', app1.views.index, name='home'),
    url(r'^$', app1.views.solution, name='solution'),
    url(r'^a$', app1.views.solution, name='home'),


]
