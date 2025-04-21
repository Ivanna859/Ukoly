from django.shortcuts import render, redirect
from django.contrib import messages
from django.utils.translation import get_language
from .models import Service, TeamMember, Reservation
from .forms import ReservationForm





def home_view(request):
    services = Service.objects.all()
    team_members = TeamMember.objects.all()
    lang = get_language()
    return render(request, 'main/home.html', {
        'services': services,
        'team_members': team_members,
        'lang': lang,
    })

def services_view(request):
    services = Service.objects.all()
    lang = request.GET.get('lang', 'cs')
    return render(request, 'main/services.html', {
        'services': services,
        'lang': lang,
    })

def team_view(request):
    team_members = TeamMember.objects.all()
    lang = request.GET.get('lang', 'cs')
    return render(request, 'main/team.html', {
        'team_members': team_members,
        'lang': lang,
    })

def reservation_view(request):
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Rezervace byla úspěšně odeslána!")
            return redirect('reservation')
    else:
        initial_service = request.GET.get('service', '')
        form = ReservationForm(initial={'service': initial_service})
    
    return render(request, 'main/reservation.html', {'form': form})


