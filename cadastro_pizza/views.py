from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import ListView
from django.views.generic.edit import View, CreateView, UpdateView, DeleteView, ModelFormMixin
from django.core.urlresolvers import reverse_lazy

from .models import Pizza, Ingrediente
from .forms import CadastroPizzaForm

# Create your views here.

def index(request):
    return HttpResponse("Hello, world. You're at the cadastro-pizza index.")

def lista_pizzas(request):
    pizzas = Pizza.objects.all()
    return render(request, 'cadastro_pizza/lista-pizza.html', {'pizzas' : pizzas})

def lista_ingredientes(request):
    pass

class PizzaCreate(CreateView):
    model = Pizza
    form_class = CadastroPizzaForm

class PizzaUpdate(UpdateView):
    model = Pizza
    template_name_suffix = '_update_form'
    form_class = CadastroPizzaForm

class PizzaDelete(DeleteView):
    model = Pizza
    success_url = reverse_lazy('lista-pizzas')

class CadastroIngredienteView(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse('Testando get')

    def post(self, *args, **kwargs):
        return HttpResponse('Testando post')