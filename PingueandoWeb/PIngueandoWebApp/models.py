from django.db import models

# Create your models here.
class Pinguer(models.Model):
    name = models.CharField(max_length=128)

class PinguerEvent(models.Model):
    EVENT_TYPE = [
    (1, 'Activation'),
    (2, 'Deactivation'),
    ]
    pinguer=models.ForeignKey(Pinguer, on_delete=models.CASCADE )
    event_type = models.IntegerField(max_length=1, choices=EVENT_TYPE)
    event_date = models.DateField()