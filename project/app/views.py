from django.shortcuts import render
from django.http import HttpResponse

def menu(req, table):
    return render(req, 'app/menu.html', {})