from django.core.urlresolvers import reverse
from django.db import models

# Create your models here.

class Ingrediente(models.Model):
    nome = models.CharField('nome', max_length=100, null=False, blank=False)
    descricao = models.CharField('descrição', max_length=255, null=False, blank=False)

    def __str__(self):
        return self.nome

    class Meta:
        db_table = 'ingredientes'
        verbose_name = 'Ingrediente'
        verbose_name_plural = 'Ingredientes'

class Pizza(models.Model):
    sabor = models.CharField('sabor', max_length=100, null=False, blank=False, unique=True)
    descricao = models.CharField('descrição', max_length=255, null=False, blank=False)
    ingredientes = models.ManyToManyField(Ingrediente, verbose_name='ingredientes', blank=True)

    def get_absolute_url(self):
        return reverse('pizzas:lista-pizzas')

    def __str__(self):
        return self.sabor

    class Meta:
        db_table = 'pizzas'
        verbose_name = 'Pizza'
        verbose_name_plural = 'Pizzas'
