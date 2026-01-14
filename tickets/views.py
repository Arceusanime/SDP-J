from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Race, Ticket, Booking
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

def race_list(request):
    races = Race.objects.all()
    return render(request, 'race_list.html', {'races': races})


def ticket_list(request, race_id):
    tickets = Ticket.objects.filter(race_id=race_id)
    race = Race.objects.get(id=race_id)
    return render(request, 'ticket_list.html', {
        'tickets': tickets,
        'race': race
    })


@login_required(login_url='/login/')
def book_ticket(request, ticket_id):
    ticket = Ticket.objects.get(id=ticket_id)

    if request.method == 'POST':
        quantity = int(request.POST['quantity'])

        if quantity > ticket.seats_left():
            messages.error(request, 'Not enough seats available.')
            return redirect(request.path)

        Booking.objects.create(
            user=request.user,
            customer_name=request.user.username,
            email=request.user.email,
            ticket=ticket,
            quantity=quantity
        )
        return redirect('booking_success', ticket_id=ticket.id)

    return render(request, 'book_ticket.html', {'ticket': ticket})


def book_ticket(request, ticket_id):
    ticket = Ticket.objects.get(id=ticket_id)

    if request.method == 'POST':
        quantity = int(request.POST['quantity'])

        if quantity > ticket.seats_left():
            messages.error(request, 'Not enough seats available.')
            return redirect(request.path)

        Booking.objects.create(
            user=request.user,   
            customer_name=request.POST['name'],
            email=request.POST['email'],
            ticket=ticket,
            quantity=quantity
        )
        return redirect('booking_success', ticket_id=ticket.id)

    return render(request, 'book_ticket.html', {'ticket': ticket})

def booking_success(request, ticket_id):
    ticket = Ticket.objects.get(id=ticket_id)
    return render(request, 'booking_success.html', {'ticket': ticket})

@login_required(login_url='/login/')
def my_bookings(request):
    bookings = Booking.objects.filter(user=request.user)
    return render(request, 'my_bookings.html', {
        'bookings': bookings
    })

def race_detail(request, race_id):
    race = Race.objects.get(id=race_id)
    tickets = Ticket.objects.filter(race=race)
    return render(request, 'race_detail.html', {
        'race': race,
        'tickets': tickets
    })

def signup_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("race_list")
    else:
        form = UserCreationForm()

    return render(request, "signup.html", {
        "form": form
    })
