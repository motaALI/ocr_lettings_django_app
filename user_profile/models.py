# profile/models.py
from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    """
    Modèle représentant le profil d'un utilisateur.

    Attributes:
        user (User): Lien OneToOne avec le modèle User.
        favorite_city (str): Champ de caractères représentant la ville préférée de l'utilisateur.
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    favorite_city = models.CharField(max_length=64, blank=True)

    def __str__(self):
        return self.user.username