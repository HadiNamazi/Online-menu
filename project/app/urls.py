from django.urls import path
from . import views

urlpatterns = [
    path('menu/<str:table>', views.menu, name='menu'),
]
