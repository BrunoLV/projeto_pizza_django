from django.contrib import admin

from .models import Pizza, Ingrediente, ValorPizza

# Register your models here.

admin.site.register(Pizza)
admin.site.register(Ingrediente)
admin.site.register(ValorPizza)
