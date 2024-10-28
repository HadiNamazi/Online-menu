from django.shortcuts import render
from . import models

def menu(req, table):
    items = models.Item.objects.all()
    categories = models.Category.objects.all()
    context = {
        'items': items,
        'categories': categories,
    }
    return render(req, 'app/menu.html', context)