#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Gestion_Pharma.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()

from bibliotheque.models import Livre

# Créer une nouvelle instance du modèle Livre
nouveau_livre = Livre(titre='Le Petit Prince', auteur='Antoine de Saint-Exupéry', date_publication='1943-04-06')

# Enregistrer l'instance dans la base de données
nouveau_livre.save()

