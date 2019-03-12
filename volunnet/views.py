from django.shortcuts import render
from .models import *
from .forms import *
from django.contrib.auth.decorators import login_required

<<<<<<< HEAD

@login_required
=======
from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect

now = timezone.now()
def home(request):
   return render(request, 'volunnet/home.html',
                 {'volunnet': home})


>>>>>>> ab92afad97668fc316e45de48a75c10dac67e8e7
def activity_list(request):
    activity = Activity.objects.filter(published_date__lte=timezone.now())
    return render(request, 'volunnet/activity_list.html',
                 {'activities': activity})

<<<<<<< HEAD

@login_required
=======
@login_required
def activity_new(request):
   if request.method == "POST":
       form = ActivityForm(request.POST)
       if form.is_valid():
           activity = form.save(commit=False)
           activity.published_date = timezone.now()
           activity.save()
           activity = Activity.objects.filter(published_date__lte=timezone.now())
           return render(request, 'volunnet/activity_list.html',{'activities': activity})
   else:
       form = ActivityForm()
       # print("Else")
   return render(request, 'volunnet/activity_new.html', {'form': form})


>>>>>>> ab92afad97668fc316e45de48a75c10dac67e8e7
def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            return render(request, 'registration/register_done.html', {'user': user})
    else:
        form = UserRegistrationForm()
    return render(request, 'registration/register.html', {'form': form})
