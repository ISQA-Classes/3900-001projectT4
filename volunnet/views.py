from django.shortcuts import render
from .models import *
from .forms import *
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from .forms import UserRegistrationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import HttpResponseRedirect

def logoutUser(request):
   logout(request)
   return HttpResponseRedirect('/home/')

organizer = True

def whoAmI(current_user):
    global organizer
    org = Organization.objects.all().filter(user=current_user)
    print(org)
    if org:
        organizer = True
        return True
    else:
        organizer = False
        return False

now = timezone.now()
def home(request):
   return render(request, 'volunnet/home.html',
                 {'volunnet': home})


def activity_list(request):
    global organizer
    print("The current value is:", organizer)
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

def signupas(request):
    return render(request, 'registration/signupas.html')

def OrganizationRegister(request):
    print("Running")
    if request.method == 'POST':
        form = OrganizationRegistrationForm(request.POST)
        if form.is_valid():
            newuser = User(username = form.cleaned_data['username'], email = form.cleaned_data['email'])
            newuser.set_password(form.cleaned_data['password'])
            newuser.save()
            org = Organization(user=newuser,name = form.cleaned_data['name'], address = form.cleaned_data['address'], state = form.cleaned_data['state'], city = form.cleaned_data['city'],phone = form.cleaned_data['phone'],zipcode = form.cleaned_data['zipcode'],email =form.cleaned_data['email'])
            org.save()
            return render(request, 'registration/register_done.html', {'user': newuser})
    else:
        form = OrganizationRegistrationForm()
    return render(request, 'registration/register.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        form =  LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'],password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return render(request, 'volunnet/home.html', {'amIorg':whoAmI(request.user)})
            else:
                form = LoginForm()
                return render(request, 'registration/login.html', {'form':form})

    else:
        form = LoginForm()
        return render(request, 'registration/login.html', {'form':form})


@login_required
def profile(request):
    return render(request, 'registration/profile.html')
