from django.shortcuts import render
from . import models

def menu(req, table):
    items = models.Item.objects.all()
    categories = models.Category.objects.all()
    general_infos = models.GeneralInfo.objects.get()
    context = {
        'items': items,
        'categories': categories,
        'general_infos': general_infos,
    }
    return render(req, 'app/menu.html', context)