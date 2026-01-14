from django.db import models
from django.conf import settings
from django.db.models import Sum


class Race(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    race_date = models.DateField()
    circuit_image = models.ImageField(
        upload_to="circuits/",
        null=True,
        blank=True
    )

    def __str__(self):
        return self.name


class Ticket(models.Model):
    race = models.ForeignKey(Race, on_delete=models.CASCADE)
    category = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    total_seats = models.PositiveIntegerField()

    @property
    def seats_left(self):
        booked = Booking.objects.filter(
            ticket=self
        ).aggregate(total=Sum("quantity"))["total"] or 0
        return self.total_seats - booked

    def __str__(self):
        return f"{self.race.name} - {self.category}"


class Booking(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )
    customer_name = models.CharField(max_length=100)
    email = models.EmailField()
    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    booked_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.customer_name
