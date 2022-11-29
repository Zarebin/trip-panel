from django.db import models

# Create your models here.

class hotell(models.Model):
    hotel_name     = models.CharField(max_length=50)
    hottl_address  = models.CharField(max_length=250)
    hotel_pics     = models.ImageField( null= True, blank=True , upload_to='images/' )
    timestamp      = models.DateTimeField(auto_now_add=True)
    hotel_info     = models.TextField()

    


    def __str__(self) -> str:
        return self.hotelname