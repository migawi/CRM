from django.shortcuts import render, redirect

from team.models import Team

from .forms import SignupForm

# Create your views here.

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)

        if form.is_valid():
            user = form.save()
            Userprofile.objects.create(user=user)

            team = Team.objects.create(name='Team name', created_by=request.usr)
            team.members.add(request.user)
            team.save()

            return redirect('login')

    else:
        form = SignupForm()

    context = {
        'form': form
    }

    return render (request, 'userprofile/signup.html', context)