from django.db import models

# Create your models here.
class ContactUS( models.Model ):
    first_name = models.CharField( max_length= 100)
    last_name = models.CharField( max_length=100 )
    email = models.EmailField(max_length=254)
    message = models.TextField()
    date = models.DateField()

    def __str__(self) -> str:
        return self.first_name +"_"+ self.last_name+ self.id