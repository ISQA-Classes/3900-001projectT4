from django.shortcuts import render
from .models import *
from .forms import *
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect


now = timezone.now()
def home(request):
   return render(request, 'volunnet/home.html',
                 {'volunnet': home})


def activity_list(request):
    activity = Activity.objects.filter(published_date__lte=timezone.now())
    return render(request, 'volunnet/activity_list.html',
                 {'activities': activity})


@login_required
def activity_new(request):
   if request.method == "POST":
       form = ActivityForm(request.POST)
       if form.is_valid():
           activity = form.save(commit=False)
           activity.published_date = timezone.now()
           activity.save()
           activity = Activity.objects.filter(published_date__lte=timezone.now())
           return render(request, 'volunnet/activity_list.html',
                         {'activities': activity})
   else:
       form = ActivityForm()
       # print("Else")
   return render(request, 'volunnet/activity_new.html', {'form': form})

@login_required
def activity_edit(request, pk):
   activity = get_object_or_404(Activity, pk=pk)
   if request.method == "POST":
       # update
       form = ActivityForm(request.POST, instance=activity)
       if form.is_valid():
           activity = form.save(commit=False)
           activity.updated_date = timezone.now()
           activity.save()
           activity = Activity.objects.filter(published_date__lte=timezone.now())
           return render(request, 'volunnet/activity_list.html',
                         {'activities': activity})
   else:
        # edit
       form = ActivityForm(instance=activity)
   return render(request, 'volunnet/activity_edit.html', {'form': form})

@login_required
def activity_delete(request, pk):
   activity = get_object_or_404(Activity, pk=pk)
   activity.delete()
   return redirect('volunnet:activity_list')

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
