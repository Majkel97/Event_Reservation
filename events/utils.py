from django.core.mail import send_mail
from django.conf import settings


def send_confirmation_email(event_data, currentuser, reservation_data):
    """
    Sends a confirmation email for a reservation to the specified user.

    Args:
        event_data (Event): The event data for which the reservation is made.
        currentuser (User): The user for whom the reservation is created.
        reservation_data (Reservation): The reservation data.

    The email contains reservation details and a cancellation link.

    Example:
    send_confirmation_email(event_instance, user_instance, reservation_instance)
    """
    cancel_link = str(
        "http://127.0.0.1:8000/delete?user={user}&reservation={reservation}"
    ).format(user=currentuser.id, reservation=reservation_data.id)
    subject = 'Twoja rezerwacja na event "' + event_data.name + '" została utworzona'
    message = """Dane rezerwacji: \nNazwa: {name} \nData rozpoczącia: {start_date}\nData zakończenia: {end_date}
                \nJeżeli chcesz anulować swoją rezerwację, skorzystaj z linku poniżej:
                \n{link}
                """.format(
        name=event_data.name,
        start_date=event_data.start_date,
        end_date=event_data.end_date,
        link=cancel_link,
    )
    mail_to = currentuser.email
    mail_from = getattr(settings, "DEFAULT_EMAIL", "")
    send_mail(subject, message, mail_from, [mail_to], fail_silently=False)
