from django.contrib import admin
from django.urls import path
from core.views import *

urlpatterns = [
    path('', index, name='index'),
    path('contato', contato, name='contato'),
    path('produto', produto, name='produto'),
]