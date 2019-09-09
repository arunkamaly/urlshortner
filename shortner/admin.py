from django.contrib import admin
from .models import *
# Register your models here.


class urldetailsAdmin(admin.ModelAdmin):
    list_display = ('fullurl', 'urlname', 'shorturl', 'createdOn')
    list_filter = ['createdOn']
    search_fields = ['fullurl']

admin.site.register(urldetails, urldetailsAdmin)
