from django.shortcuts import render
from .models import Info, Point, Picture
from django.http import HttpResponseRedirect
from django.urls import reverse

def home(request):
    points_list = Point.objects.all()
    info_list = Info.objects.all()
    picture_list = Picture.objects.all()
    context = {'points_list': points_list, 'info_list': info_list, 'picture_list':picture_list}
    return render(request, 'place/home.html', context)


def submit(request):
    formInfo = Info()
    formInfo.name = request.POST.get('placenameinput')
    formInfo.description = request.POST.get('descriptioninput')
    formInfo.save()
    formPoint = Point()
    formPoint.info = Info.objects.get(name=request.POST.get('placenameinput'))
    formPoint.latitude = request.POST.get('latitudeinput')
    formPoint.longitude = request.POST.get('longitudeinput')
    formPoint.save()
    formPicture = Picture()
    formPicture.info = Info.objects.get(name=request.POST.get('placenameinput'))
    formPicture.picture = request.POST.get('image')
    formPicture.save()

    # Always return an HttpResponseRedirect after successfully dealing
    # with POST data. This prevents data from being posted twice if a
    # user hits the Back button.
    return HttpResponseRedirect(reverse('home'))

##########################
# Add to the submit form the name of the user who create the Plazee
# Should the restriction for postig should be through the submit
#function with a login required decorator?
#or a simple html if statement?