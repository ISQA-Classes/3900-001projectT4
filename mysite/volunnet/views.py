from django.shortcuts import render
from .models import *
from .forms import *


def activity_list(request):
    activity = Activity.objects.filter(published_date__lte=timezone.now())
    return render(request, 'volunnet/activity_list.html',
                 {'activities': activity})
