from django.shortcuts import render, redirect

from django.contrib.auth import login,authenticate, logout
from django.contrib import messages

import re
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User



# fonction pour créer un compte 

def Creation_Compte(request):

    if request.method ==  "POST":

        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password_confirm = request.POST['password_confirm']

        # verification des mots de passe

        if password != password_confirm:
            messages.error(request, "Les mots de passe ne sont pas identiques. veuillez réessayer.")
            return redirect ("creation")

        # verification de la longeur et des caractères du mot de passe  

        if len(password) < 8 or not re.search(r'[A-Za-z]', password) or not re.search(r'\d', password) or not re.search(r'[!@#$%(),.?":{}`|<>]', password):
            messages.error(request, 'Le mot de passse doit contenir au moins 8 caractères, incluant des lettres, des chiffres et des caractères spéciaux.')
            return redirect("creation")
        
        # verification du format de l'adresse mail

        try:
            validate_email(email)
        except ValidationError:
            messages.error(request, "L'adresse e-mail invalide. Veuillez réessayer.")
            return redirect("creation")
        
        # verification de l'existence de l'utilisateur et de l'adresse mail
        
        if User.objects.filter(username=username).exists():
            messages.error(request, "Ce nom d'utilisateur existe déjà. Veuillez réessayer.")
            return redirect("creation")
        
        if User.objects.filter(email=email).exists():
            messages.error(request, "Cette adresse e-mail est déjà utilisée. Veuullez en choisir une autre.")
            return redirect("creation")
        
        # création de l'utilisateur

        User.objects.create_user(username=username, email=email, password=password)
        messages.success(request, "Compte crée avec succès. Connectez-vous maintenant.")

        return redirect('login')
    
    return render(request, "creation.html")


# fonction pour se connecter

def Connecter_Compte(request):

    if request.method == 'POST':

        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username = username, password = password)

        if user is not None:
            login(request, user)
            return redirect('acc')
        
        else:
            messages.error(request, "Nom d'utilisateur ou le mot de passe incorect.")
            return redirect("login")
    return render (request, 'login.html')


# fonction pour la vérification de l'adresse mail

def Verification_Mail(request):

    if request.method == "POST":

        email = request.POST.get('email')

        # verification si l'email 

        if not email:
            messages.error(request, "Veuillez rentrer une adresse mail valide.")
            return (request, "verificaionMail.html")
        
        user = User.objects.filter(email=email).first

        if user:

            return redirect("modifierCode", email=email)
        
        else:
            messages.error(request, "Cette adresse ne correspond à aucun compte. Veuillez réessayez avec une autre ou créez un compte")
            return redirect("verification")
        

    
    return render(request, "verificaionMail.html")


# fonction pour changer le mot de passe après vérifiction

def Changement_Code(request, email):

    try:
        user = User.objects.get(email=email)

    except User.DoesNotExist:
        messages.error(request, "L'utilisateur Introuvable.")
        return redirect("verification")
    
    if request.method == "POST":

        password = request.POST.get('password')
        password_confirm = request.POST.get('password_confirm')


        if password == password_confirm:

            if len(password) < 8:
                messages.error(request, "Le mot de passe doit contenir au moins 8 caractères.")

            elif not any(char.isdigit() for char in password):

                messages.error(request, "Le mot de passe doit contenir au moins un chiffre")

            elif not any(char.isalpha() for char in password):

                messages.error(request, "Le mot de passe doit contenir au moins une lettre.")

            else:
                user.set_password(password)
                user.save()
                messages.success(request, "Le mot de passe a bien été modifié. Connectez-vous maintenant")

                return redirect("login")


        else:
            messages.error(request, "Les mots de passe ne correspondent pas. Réessayez")

            
    
    context = {
            'email':email
        }
    return render(request, "nouveauMDP.html", context)



# fonction pour la deconnection

def Deconnection(request):

    logout(request)
    return redirect("login")
