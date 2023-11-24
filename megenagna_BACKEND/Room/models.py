from django.db import models

# Create your models here.
class RoomProfile(models.Model):
    name = models.CharField(max_length=500)
    description = models.TextField()
    capacity = models.IntegerField()
    bedNumber = models.IntegerField()
    availability_status = models.BooleanField(default=True)
    price = models.IntegerField(null=True)
    services = models.TextField(max_length= 200)
    image = models.ImageField(upload_to='room_image/')

    def __str__(self):
        return self.name

class Room(models.Model):
    name = models.CharField(max_length=500)
    room_profile =  models.ForeignKey(RoomProfile, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name
