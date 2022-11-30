from django.contrib import admin
from django.utils.html import format_html
from adminpanel.models import Hotel


@admin.register(Hotel)
class HotelAdmin(admin.ModelAdmin):
    list_display = ['id', 'hotel_name',  'score', 'insert_time','hotel_pictures', ]
    fields = ['hotel_name', 'hotel_pictures', ('hotel_info', 'hotel_address'), 'score',  ]
    sortable_by = ['hotel_name', 'score', 'insert_time']
    list_editable = ['score']
    list_filter = ['hotel_address']
    search_fields = ['hotel_name']


    def image_tag(self, obj):

        return format_html('<img src="{}" width="200" height="200"/>'.format(obj.hotel_pictures.url))

    image_tag.short_description = 'Image'



