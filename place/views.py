from django.shortcuts import render
from .models import Point
from .models import Info


def home(request):
    points_list = Point.objects.all()
    info_list = Info.objects.all()
    context = {'points_list': points_list, 'info_list': info_list}
    return render(request, 'place/home.html', context)