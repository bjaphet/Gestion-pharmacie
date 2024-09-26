from django.contrib import admin

from .models import *


admin.site.register(Categories)
admin.site.register(Produits)
admin.site.register(Vente)
admin.site.register(Facture_Client)
admin.site.register(Customer)


