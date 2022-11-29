from django.contrib import admin
from adminpanel.models import Hotel

@admin.register(Hotel)
class HotelAdmin(admin.ModelAdmin):
    list_display = ['id', 'hotel_name',  'score', 'insert_time', ]
    fields = ['hotel_name', 'hotel_pictures', ('hotel_info', 'hotel_address'), 'score']
    sortable_by = ['hotel_name', 'score', 'insert_time']
    list_editable = ['score']
    list_filter = ['hotel_address']
    search_fields = ['hotel_name']


