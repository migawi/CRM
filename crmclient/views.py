import csv
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect

from .models import Client
from .forms import AddClientForm, AddCommentForm, AddFileForm
from team.models import Team

# Create your views here.

@login_required
def client_export(request):
    clients = Client.objects.filter(created_by=request.user)

    response = HttpResponse(
        content_type='text/csv',
        headers={
            'Content-Disposition': 'attachment; filename="clients.csv"'
        },
    )
    writer = csv.writer(response)
    writer.writerow(['Client', 'Definition', 'Created_at', 'Created_by'])

    for client in clients:
        writer.writerow([client.name, client.definition, client.created_at, client.created_by])

    return response

@login_required
def client_catalog(request):
    clients = Client.objects.filter(created_by=request.user)

    context = {'clients': clients}

    return render(request, 'crmclient/clients.html', context)

@login_required
def client_detail(request, pk):
    client = get_object_or_404(Client, created_by=request.user, pk=pk)
    team = Team.objects.filter(created_by=request.user)[0]

    if request.method == 'POST':
        form = AddCommentForm(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.team = team
            comment.created_by = request.user
            comment.client = client
            comment.save()

            return redirect('client_detail', pk=pk)

    else:
        form = AddCommentForm()

    context = {'client': client, 'form': form, 'form2': AddFileForm(),}

    return render(request, 'crmclient/client_detail.html', context)

@login_required
def new_client(request):
    team = Team.objects.filter(created_by=request.user)[0]
    if request.method == 'POST':
        form = AddClientForm(request.POST)

        if form.is_valid():
            team = Team.objects.filter(created_by=request.user)[0]
            client = form.save(commit=False)
            client.created_by = request.user
            client.team = team
            client.save()

            messages.success(request, 'Client created successfully.')

            return redirect('clients')
    else:
        form = AddClientForm()

    return render(request, 'crmclient/new_client.html', {
        'form': form,
        'team': team,
    })

@login_required
def edit_clients(request, pk):
    client = get_object_or_404(Client, created_by=request.user, pk=pk)
    if request.method == 'POST':
        form = AddClientForm(request.POST, instance=client)

        if form.is_valid():
            client.save()

            messages.success(request, 'Client details edditted successfully.')

            return redirect('clients')
    else:
        form = AddClientForm(instance=client)

    return render(request, 'crmclient/edit_clients.html', {
        'form': form
    })

@login_required
def delete_clients(request, pk):
    client = get_object_or_404(Client, created_by=request.user, pk=pk)
    client.delete()

    messages.success(request, 'Client deleted.')

    return redirect('clients')

@login_required
def add_client_file(request, pk):
    client = get_object_or_404(Client, created_by=request.user, pk=pk)
    team = Team.objects.filter(created_by=request.user)[0]

    if request.method == 'POST':
        form = AddFileForm(request.POST, request.FILES)

        if form.is_valid():
            file = form.save(commit=False)
            file.team = team
            file.created_by = request.user
            file.client_id = pk
            file.save()

            return redirect('clients')
    return redirect('clients')
