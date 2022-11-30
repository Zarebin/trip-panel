from django.db import models
from django.utils.html import escape



class Hotel(models.Model):
    hotel_name     = models.CharField(max_length=100)
    hotel_pictures    = models.ImageField( null= True, blank=True , upload_to='images/' )
    insert_time     = models.DateTimeField(auto_now_add=True)
    hotel_info    = models.TextField()
    score = models.PositiveSmallIntegerField(max_length=1)
    hotel_address = models.CharField(max_length=550)

    
    def image_tag(self):
        return u'<img src="%s" />' % escape(self.hotel_pictures.url)


    image_tag.short_description = 'hotel_pictures'
    image_tag.allow_tags = True


    def __str__(self) -> str:
        return self.hotel_name