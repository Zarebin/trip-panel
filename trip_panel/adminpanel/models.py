from django.db import models



class Hotel(models.Model):
    hotel_name     = models.CharField(max_length=100)
    hotel_pictures    = models.ImageField( null= True, blank=True , upload_to='images/' )
    insert_time     = models.DateTimeField(auto_now_add=True)
    hotel_info    = models.TextField()
    score = models.PositiveSmallIntegerField(max_length=1)
    hotel_address = models.CharField(max_length=550)

    


    def __str__(self) -> str:
        return self.hotel_name