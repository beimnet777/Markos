from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField( max_length= 500 )
    body = models.TextField()
    image = models.ImageField()
    date = models.DateField('blog_image/')

    def __str__(self) -> str:
        return self.title + str(self.date)

