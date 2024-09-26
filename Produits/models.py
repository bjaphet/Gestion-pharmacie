from django.db import models



class Categories(models.Model):
    name= models.CharField(max_length=250)
    def __str__(self):
        return self.name

# class pour les produits 

class Produits(models.Model):
    
    name = models.CharField(max_length= 100)
    category= models.ForeignKey(Categories, on_delete=models.CASCADE)
    price = models.IntegerField()
    quantite=models.PositiveIntegerField(default=0)
    description= models.TextField()
    date_ajout= models.DateTimeField(auto_now_add=True)
    date_expiration= models.DateField()
    image=models.ImageField(null=True,blank=True)
    
    class Meta:
        ordering =['-date_ajout']

    
    def statut_quantite(self):

        #si la quantute est égale à affiche rouge

        if self.quantite == 0:
            return 'red'
        
        # sinon si la quantite est inféreiur ou egale à 10 affiche orange

        elif self.quantite <= 10:
            return 'orange'
        
        else: 
            return 'green'
    def __str__(self):
        return self.name
        
class Customer(models.Model):
    name= models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Vente(models.Model):
    produit = models.ForeignKey(Produits, on_delete= models.CASCADE)
    sale_date = models.DateTimeField(auto_now_add=True)
    quantite = models.PositiveIntegerField()
    customer = models.CharField(max_length=100)
    total_amount = models.DecimalField(max_digits= 10, decimal_places=2)

    def __str__(self):
        return self.produit
    



class Facture_Client(models.Model):
    customer = models.ForeignKey(Customer, on_delete= models.CASCADE)
    quantite = models.PositiveIntegerField()
    date_achat= models.DateTimeField(auto_now_add=False)
    total_amount = models.ForeignKey(Vente, on_delete= models.CASCADE)
    produit= models.ForeignKey(Produits, on_delete=models.CASCADE)

    def __str__(self) :
        return f"Le reçu de {self.customer.customer}"
    
