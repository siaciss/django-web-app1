from django.contrib import admin
from listings.models import Band,Listing

class BandAdmin(admin.ModelAdmin):
    #liste des champs que nous voulons sur l'affichage de la liste
    list_display = ('name','year_formed','genre')

admin.site.register(Band, BandAdmin)

class ListingAdmin(admin.ModelAdmin):
    list_display = ('title','sold','year','type','band')

admin.site.register(Listing, ListingAdmin)