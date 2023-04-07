from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

from team.models import Team

# Create your views here.

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            user = form.save()
            Userprofile.objects.create(user=user)

            team = Team.objects.create(name='Team name', created_by=request.usr)
            team.members.add(request.user)
            team.save()

            return redirect('login')

    else:
        form = UserCreationForm()

    context = {
        'form': form
    }

    return render (request, 'userprofile/signup.html', context)