from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import ListView
from django.views.generic.edit import DeleteView, ModelFormMixin
from django.core.urlresolvers import reverse_lazy
from django.forms import inlineformset_factory

from .models import Pizza, Ingrediente, ValorPizza
from .forms import CadastroPizzaForm, CadastroIngredienteForm

# Create your views here.

def index(request):
    return HttpResponse("Hello, world. You're at the cadastro-pizza index.")

def lista_pizzas(request):
    template_name = 'cadastro_pizza/lista-pizza.html'
    pizzas = Pizza.objects.all()
    context = {}
    context['pizzas'] = pizzas
    return render(request, template_name, context)

def cardapio(request):
    template_name = 'cadastro_pizza/cardapio.html'
    pizzas = Pizza.objects.all()
    context = {}
    context['pizzas'] = pizzas
    return render(request, template_name, context)

def lista_ingredientes(request):
    pass

def nova_pizza_2(request):
    template_name = 'cadastro_pizza/cadastro-pizza-2.html'
    PizzaFormSet = inlineformset_factory(Pizza, ValorPizza, fields=('quantia', 'tamanho_pizza'), extra=2)
    context = {}
    if request.method == 'GET':
        form = CadastroPizzaForm(instance=Pizza())
        formset = PizzaFormSet(instance=Pizza(), initial=[{'quantia': 0.00, 'tamanho_pizza': 1,}])
        context['form'] = form
        context['formset'] = formset
        return render(request, template_name, context)
    if request.method == 'POST':
        form = CadastroPizzaForm(request.POST)
        if form.is_valid():
            pizza = form.save()
            formset = PizzaFormSet(request.POST, request.FILES, instance=pizza)
            if formset.is_valid():
                for form in formset:
                    if form.is_valid():
                        form.save()
                return redirect('pizzas:lista-pizzas')

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