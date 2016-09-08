from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import ListView
from django.views.generic.edit import DeleteView, ModelFormMixin
from django.core.urlresolvers import reverse_lazy

from .models import Pizza, Ingrediente
from .forms import CadastroPizzaForm, CadastroIngredienteForm

# Create your views here.

def index(request):
    return HttpResponse("Hello, world. You're at the cadastro-pizza index.")

def lista_pizzas(request):
    pizzas = Pizza.objects.all()
    return render(request, 'cadastro_pizza/lista-pizza.html', {'pizzas' : pizzas})

def lista_ingredientes(request):
    pass

def nova_pizza(request):
    template_name = 'cadastro_pizza/cadastro-pizza.html'
    context = {}
    if request.method == 'GET':
        context['form'] = CadastroPizzaForm
        return render(request, template_name, context)
    if request.method == 'POST':
        form = CadastroPizzaForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect('pizzas:lista-pizzas')

def edita_pizza(request,pk):
    template_name = 'cadastro_pizza/cadastro-pizza.html'
    context = {}
    if request.method == 'GET':
        context['form'] = CadastroPizzaForm(instance=Pizza.objects.get(pk=pk))
        return render(request, template_name, context)
    if request.method == 'POST':
        form = CadastroPizzaForm(request.POST, instance=Pizza.objects.get(pk=pk))
        if form.is_valid:
            form.save()
            return redirect('pizzas:lista-pizzas')    
    
def novo_ingrediente(request):
    template_name = 'cadastro_pizza/cadastro-ingrediente.html'
    context = {
        'form':CadastroIngredienteForm
    }
    if request.method == 'GET':
        return render(request, template_name, context)
    if request.method == 'POST':
        form = CadastroIngredienteForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect('pizzas:lista-pizzas')

class PizzaDelete(DeleteView):
    model = Pizza
    success_url = reverse_lazy('pizzas:lista-pizzas')