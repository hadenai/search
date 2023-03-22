from django.db import models

class Produit(models.Model):
    ingredient = models.TextField()
    countries = models.TextField(default='france')
    nutri_score = models.TextField(default='a')
    marque = models.TextField(default='marque')
    name = models.TextField(default='toto')
    

