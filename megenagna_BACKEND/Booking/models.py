from django.db import models
from Room.models import Room
from datetime import datetime
import uuid

# Create your models here.
class Booking(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
    ]
    Currency_Choice = [('usd', 'USD'),
                       ('etb',"ETB")]
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    customer_first_name = models.CharField(max_length = 500)
    customer_last_name = models.CharField(max_length=500)
    customer_email = models.EmailField()
    customer_phone_number = models.CharField(max_length= 20)
    start_date = models.DateField()
    end_date = models.DateField()
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    currency  = models.CharField(choices= Currency_Choice, max_length= 10)
    payment_status = models.CharField(choices= STATUS_CHOICES, default= 'pending', max_length= 10)
    total_amount = models.IntegerField()
    created_at = models.DateField(auto_now_add=True)

    def __str__(self) -> str:
        return "Booknig" + str(self.id) + "___Payment_status___" + self.payment_status
    
    
        


    