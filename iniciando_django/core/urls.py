from django.urls import path
from .views import index, contato, produto

urlpatterns = [
    path('', index),
    path('contato', contato),
    path('produto/<int:produto_id>', produto, name="produto"),
]