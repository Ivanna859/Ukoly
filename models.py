from django.db import models

class TeamMember(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    bio = models.TextField()
    image = models.ImageField(upload_to='team_photos/', null=True, blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Service(models.Model):
    CATEGORY_CHOICES = [
        ('haircut', 'Střihy'),
        ('beard', 'Vousy'),
        ('extra', 'Extra služby'),
    ]

    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='haircut')
    name = models.CharField(max_length=100)
    name_en = models.CharField(max_length=100, blank=True, null=True)
    name_ua = models.CharField(max_length=100, blank=True, null=True)
    description = models.TextField(blank=True)
    description_en = models.TextField(blank=True, null=True)
    description_ua = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.name

class Reservation(models.Model):
    customer_name = models.CharField(max_length=100)
    customer_email = models.EmailField()
    customer_phone = models.CharField(max_length=20)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    team_member = models.ForeignKey(TeamMember, on_delete=models.CASCADE, null=True, blank=True)
    date = models.DateField()
    time = models.TimeField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Rezervace pro {self.customer_name} na {self.date} v {self.time}"
