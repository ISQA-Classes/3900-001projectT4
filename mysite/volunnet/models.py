from django.conf import settings
from django.db import models
from django.utils import timezone
import uuid


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


class Activity(models.Model):
    activityID = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
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
