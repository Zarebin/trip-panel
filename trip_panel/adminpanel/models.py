from django.db import models

# Create your models here.

class hotell(models.Model):
    hotelname     = models.CharField(max_length=50)
    hotellpics    = models.ImageField( null= True, blank=True , upload_to='images/' )
    timestamp     = models.DateTimeField(auto_now_add=True)
    date          = models.DateTimeField(auto_now_add=True)
    hotellinfo    = models.TextField()

    


    def __str__(self) -> str:
        return self.hotelname