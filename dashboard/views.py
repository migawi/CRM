from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from lead.models import Lead
from crmclient.models import Client
from team.models import Team

# Create your views here.

@login_required
def dashboard(request):
    team = Team.objects.filter(created_by=request.user)[0]
    leads = Lead.objects.filter(team=team, converted_to_client=False).order_by('-created_at')[0:5]
    clients = Client.objects.filter(team=team).order_by('-created_at')[0:5]

    context = {
        'team': team,
        'leads': leads,
        'clients': clients,
    }
    return render(request, 'userprofile/dashboard.html', context)