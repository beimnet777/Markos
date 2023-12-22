from django.db import models

# Create your models here.
class ContactUS( models.Model ):
    name = models.CharField( max_length= 100)
    email = models.EmailField(max_length=254)
    message = models.TextField()
    date = models.DateField()

    def __str__(self) -> str:
        return  self.name+ "         "  + str(self.date)