from django.shortcuts import render
from .models import *
from .forms import *
from django.contrib.auth.decorators import login_required

@login_required
def activity_list(request):
    activity = Activity.objects.filter(published_date__lte=timezone.now())
    return render(request, 'volunnet/activity_list.html',
                 {'activities': activity})

<<<<<<< HEAD
@login_required
=======
>>>>>>> 3671282134de46c350befa6cba2bb729b4ecf927
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
