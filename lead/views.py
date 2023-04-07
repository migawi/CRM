from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

from .forms import AddLeadForm
from .models import Lead
from crmclient.models import Client
from team.models import Team

# Create your views here.

@login_required
def leads_catalog(request):
    leads = Lead.objects.filter(created_by=request.user, converted_to_client=False)

    context = {'leads': leads}

    return render(request, 'lead/leads_catalog.html', context)

@login_required
def new_lead(request):
    team = Team.objects.filter(created_by=request.user)[0]
    if request.method == 'POST':
        form = AddLeadForm(request.POST)

        if form.is_valid():
            team = Team.objects.filter(created_by=request.user)[0]
            lead = form.save(commit=False)
            lead.created_by = request.user
            lead.team = team
            lead.save()

            messages.success(request, 'Lead has been created.')

            return redirect('leads')
    else:
        form = AddLeadForm()

    context = {
        'form': form,
        'team': team
    }

    return render(request, 'lead/new_lead.html', context)

@login_required
def leads_detail(request, pk):
    lead = get_object_or_404(Lead, created_by=request.user, pk=pk)
    #lead = Lead.objects.filter(created_by=request.user).get(pk=pk)

    context = {'lead': lead}

    return render(request, 'lead/leads_detail.html', context)

@login_required
def edit_lead(request, pk):
    lead = get_object_or_404(Lead, created_by=request.user, pk=pk)
    if request.method == 'POST':
        form = AddLeadForm(request.POST, instance=lead)

        if form.is_valid():
            lead.save()

            messages.success(request, 'Lead changes have been updated')

            return redirect('leads')
    else:
        form = AddLeadForm(instance=lead)   


    return render(request, 'lead/edit.html', {
        'form': form
    })

@login_required
def delete_lead(request, pk):
    lead = get_object_or_404(Lead, created_by=request.user, pk=pk)
    lead.delete()

    messages.success(request, 'The lead was deleted successfully.')

    return redirect('leads')

@login_required
def convert_to_client(request, pk):
    lead = get_object_or_404(Lead, created_by=request.user, pk=pk)
    team = Team.objects.filter(created_by=request.user)[0]

    client = Client.objects.create(
        name=lead.name,
        email=lead.email,
        definition=lead.definition,
        created_by=request.user,
        team=team,
    )

    lead.converted_to_client = True
    lead.save()

    messages.success(request, 'Lead has been converted to client.')

    return redirect('leads')