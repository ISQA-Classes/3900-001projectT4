from django.conf import settings
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


# How to build models
# https://docs.djangoproject.com/en/2.1/topics/db/models/
TYPE_CHOICES = (
    ('Service Learning', 'Service Learning'),
    ('Assisting Developing Country', 'Assisting Developing Country'),
    ('Virtual', 'Virtual'),
    ('Community', 'Community'),
    ('Environmental', 'Environmental'),
    ('Emergency Service', 'Emergency Service'),
    ('Educational', 'Educational'),
    ('Corporate', 'Corporate'),
    ('Event', 'Event'),
    ('Social/Welfare', 'Social/Welfare'),
)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'

class Organization(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=150)
    address = models.CharField(max_length=500)
    city = models.CharField(max_length=50, default = 'Omaha')
    state = models.CharField(max_length=2, default = 'NE')
    phone = models.IntegerField(default=1234567890)
    zipcode = models.IntegerField(default=68106)
    email = models.EmailField(blank=True)


class Activity(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    type = models.CharField(max_length=30, choices=TYPE_CHOICES)
    start_time = models.DateTimeField(default=timezone.now)
    end_time = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(default=timezone.now)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
