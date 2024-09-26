from django.urls import path
from .views import * 
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',Acc,name='acc'),

    path('produit/', Affichage.as_view(), name='home'),
    path('ajout/', AjoutProduits.as_view(), name='ajout'),
    # path('modification/<int:id>/', modifier,name='modifier'),

    path('modication/<int:pk>/', update_donnees.as_view(), name='modifier'),
    # path('supprimer/<int:id>/', supprimer, name="supprimer"),
#    path ('detail/<int:id>/', detail,name='detail'),
    path('details/<int:pk>/', edit.as_view(),name='details'),
    
    path('delete/<int:pk>/', delete.as_view(),name='delete'),

    path('recherche/', recherche, name='recherche'),

    path('ajoutvente/<int:id>/', VenteProduits, name='ajoutvente'),
    path('saverecu/<int:id>/', SaveRecu, name='saverecu'),
    path('facture/<int:sale_id>/', Facture, name='facture'),
    # path('ajout/',ajout_donnees,name='ajout'),


]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



