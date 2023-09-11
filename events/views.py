from django.shortcuts import redirect, render
from events.models import Event, Reservation
from datetime import datetime, timedelta, timezone
from events.utils import send_confirmation_email
from django.contrib.auth.decorators import login_required


def index(request):
    """
    View function for displaying a list of upcoming events and handling event reservations.

    This view retrieves a list of upcoming events, allows users to make reservations for events,
    and sends confirmation emails for successful reservations.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The HTTP response object containing the rendered template and context.
    """
    if request.method == "POST":
        event_id = request.POST.get("id")
        if event_id:
            event_data = Event.objects.get(id=event_id)
            reservation_data = Reservation.objects.create(user=request.user, event=event_data)
            current_user = request.user
            send_confirmation_email(event_data, current_user, reservation_data)
            return redirect("management")

    events = Event.objects.filter(start_date__gte=datetime.now(timezone.utc)).order_by("start_date")
    context = {"events": events}
    return render(request, "events/index.html", context)


@login_required(login_url="/signin")
def management(request):
    """
    View function for managing user reservations and checking for expired reservations.

    This view retrieves a user's reservations, and if a POST request is received, it checks
    if the reservation is expired and deletes it accordingly.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The HTTP response object containing the rendered template and context.
    """
    
    if request.method == "POST":
        event_data = request.POST["id"]
        record = Reservation.objects.get(id=event_data, user=request.user)
        expired = check_data_and_delete(record)

    reservation = Reservation.objects.filter(user=request.user)
    expired = False
    context = {"reservation": reservation, "expired": expired}
    return render(request, "events/management.html", context)


def delete(request):
    """
    View function for deleting a user's reservation and checking for expiration.

    This view handles the deletion of a user's reservation based on the provided user and reservation IDs.
    It also checks if the reservation is expired and updates the 'expired' flag accordingly.

    Args:
        request (HttpRequest): The HTTP request object. It expects 'user' and 'reservation' parameters
            in the query string (GET) and 'reservation_id' in the POST data (if a POST request is made).

    Returns:
        HttpResponse: The HTTP response object containing the rendered template and context.
    """
    expired = False
    user = request.GET["user"]
    reservation = request.GET["reservation"]
    reservation = Reservation.objects.filter(user=user, id=reservation)
    if request.method == "POST":
        event_data = request.POST["id"]
        record = Reservation.objects.get(id=event_data, user=user)
        expired = check_data_and_delete(record)

    context = {"reservation": reservation, "expired": expired}
    return render(request, "events/management.html", context)


def check_data_and_delete(record):
    """
    Checks if a reservation is expired and deletes it if it's not.

    Args:
        record (Reservation): The reservation record to check.

    Returns:
        bool: True if the reservation is expired, False otherwise.

    This function calculates the time difference between the start date of the event
    associated with the reservation and the current time. If the difference is greater
    than 2 days, the reservation is considered expired and deleted. Otherwise, it's not
    deleted, and the function returns False to indicate that it's not expired.
    """
    event_time = record.event.start_date - timedelta(days=2)
    time = datetime.now(timezone.utc)
    diffrence = event_time - time
    if diffrence.days > 0:
        record.delete()
    else:
        return True
