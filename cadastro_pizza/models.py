from django.core.urlresolvers import reverse
from django.db import models

# Create your models here.

class Ingrediente(models.Model):
    nome = models.CharField(max_length=100, null=False, blank=False)
    descricao = models.CharField(max_length=255, null=False, blank=False)

    def __str__(self):
        return self.nome

class Pizza(models.Model):
    sabor = models.CharField(max_length=100, null=False, blank=False, unique=True)
    descricao = models.CharField(max_length=255, null=False, blank=False)
    valor = models.DecimalField(null=False, max_digits=5, decimal_places=2)
    ingredientes = models.ManyToManyField(
        Ingrediente,
        through='IngredientesPizza',
    )

    def get_absolute_url(self):
        return reverse('lista-pizzas')

class IngredientesPizza(models.Model):
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    ingrediente = models.ForeignKey(Ingrediente, on_delete=models.CASCADE)