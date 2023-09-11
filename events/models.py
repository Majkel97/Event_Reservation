from django.db import models
from django.contrib.auth.models import User

# Database models:


class Event(models.Model):
    """
    Model representing an event.

    Attributes:
        name (str): The name of the event.
        image (ImageField): An image representing the event (optional).
        start_date (DateTimeField): The start date and time of the event.
        end_date (DateTimeField): The end date and time of the event.

    Meta:
        db_table (str): The database table name for this model.

    Methods:
        __str__(): Returns the name of the event.
        imageURL(): Returns the URL of the event's image (or an empty string if not available).
    """
    # id = models.UUIDField(default = uuid.uuid4, unique=True, primary_key = True, editable=False)
    name = models.CharField(max_length=150, null=True)
    image = models.ImageField(null=True, blank=True)
    start_date = models.DateTimeField(auto_now=False, auto_now_add=False)
    end_date = models.DateTimeField(auto_now=False, auto_now_add=False)

    class Meta:
        db_table = "event"

    def __str__(self):
        return self.name

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ""
        return url


class Reservation(models.Model):
    """
    Model representing a reservation for an event.

    Attributes:
        user (ForeignKey): The user who made the reservation (nullable).
        event (ForeignKey): The event for which the reservation is made (nullable).
        date (DateTimeField): The date and time when the reservation was created.

    Meta:
        db_table (str): The database table name for this model.

    Methods:
        __str__(): Returns a string representation of the reservation.
    """
    # id = models.UUIDField(default = uuid.uuid4, unique=True, primary_key = True, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=False, null=False)
    event = models.ForeignKey(Event, on_delete=models.CASCADE, blank=False, null=False)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "reservation"

    def __str__(self):
        return self.event
