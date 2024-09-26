from django.forms import ModelForm
from .models import Produits, Vente
from django import forms 


class AjoutProduit(ModelForm):
  
    class Meta:
        model = Produits
        fields = [
            'name', 'category', 'price', 'quantite', 'description', 'date_expiration', 'image'
        ]

        widgets = {
            'name': forms.TextInput(
                attrs = {
                    'placeholder': 'Entrez le nom du produit',
                    'class':'form-control'
                }
            ),

            'category': forms.Select(
                attrs={
                    'class':'form-control'
                }
            ),

            'price' : forms.NumberInput(
                attrs= {
                    'placeholder': 'Entrez le prix du prodtuit',
                    'class': 'form-control'
                }
            ),
            
            'quantite': forms.NumberInput(
                attrs={
                    'placeholder': 'Entrez la quantité',
                    'class': 'form-control'
                }
            ),
            'description': forms.Textarea(
                attrs={
                    'placeholder': 'Description',
                    'class': 'form-control',
                    'rows': 4
                }
            ),
            'date_expiration': forms.DateInput(
                attrs={
                    'placeholder': 'Date d\'expiration',
                    'class': 'form-control',
                    'type': 'date'
                }
            ),
            'image': forms.FileInput(
                attrs={
                    'class': 'form-control-file'
                }
            )
        }


    def __init__(self, *args, **kwargs):
        super(AjoutProduit, self).__init__(*args, **kwargs)
        self.fields['name'].error_messages = {
            'required': 'Le nom du produit est obligatoire',
            'invalid': 'Veuillez entrer un nom correct.'
        }
        self.fields['category'].error_messages = {
            'required': 'La catégorie est obligatoire',
            'invalid': 'Veuillez sélectionner une catégorie valide'
        }
        self.fields['price'].error_messages = {
            'required': 'Le prix du produit est obligatoire',
            'invalid': 'Veuillez entrer un prix correct.'
        }
        self.fields['quantite'].error_messages = {
            'required': 'La quantité est obligatoire.',
            'invalid': 'Veuillez entrer une quantité valide.'
        }
        self.fields['description'].error_messages = {
            'required': 'La description est obligatoire.',
            'invalid': 'Veuillez entrer une description valide.'
        }
        self.fields['date_expiration'].error_messages = {
            'required': "La date d'expiration du produit est obligatoire.",
            'invalid': 'Veuillez entrer une date d\'expiration valide.'
        }

    
# formulaire de vnete


class AjoutVente(forms.ModelForm):
    quantite = forms.IntegerField(
        help_text='Veuillez entrer la quantité de produit',
        required=True,
        error_messages={
            'required': 'La quantité est obligatoire.',
            'invalid': 'Veuillez entrer une quantité raisonnable.'
        }
    ),
 
    customer = forms.CharField(
        help_text='Veuillez entrer le nom',
        required=True,
        max_length=100,
        error_messages={
            'required': 'Le nom du client est obligatoire.',
            'invalid': 'Veuillez entrer un nom correct.'
        }
    ),
    class Meta:
        model = Vente  # Assurez-vous que le nom du modèle est correct ici
        fields = ['quantite', 'customer']

        widgets = {
            'customer': forms.TextInput(attrs={'placeholder': "Nom du client", "class": 'form-control'}),
            'quantite': forms.TextInput(attrs={'placeholder': "La quantité", "class": 'form-control'}),
        }
        