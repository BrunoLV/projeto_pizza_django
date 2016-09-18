from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic.edit import DeleteView

from .forms import CadastroPizzaForm, CadastroIngredienteForm, ValorPizzaFormSet
from .models import Pizza


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

def nova_pizza(request):
    template_name = 'cadastro_pizza/cadastro-pizza.html'
    pizza = Pizza()
    context = {}
    if request.method == 'GET':
        form = CadastroPizzaForm()
        formset = ValorPizzaFormSet(instance=pizza)
        context['form'] = form
        context['formset'] = formset
        return render(request, template_name, context)
    if request.method == 'POST':
        form = CadastroPizzaForm(request.POST)
        if form.is_valid():
            created_pizza = form.save()
            formset = ValorPizzaFormSet(request.POST, instance=created_pizza)
            if formset.is_valid():
                formset.save()
                return redirect('pizzas:lista-pizzas')


def edita_pizza(request, pk):
    template_name = 'cadastro_pizza/cadastro-pizza.html'
    pizza = Pizza.objects.get(pk=pk)
    context = {}
    if request.method == 'GET':
        form = CadastroPizzaForm(instance=pizza)
        formset = ValorPizzaFormSet(instance=pizza)
        context['form'] = form
        context['formset'] = formset
        return render(request, template_name, context)
    if request.method == 'POST':
        form = CadastroPizzaForm(request.POST, instance=pizza)
        formset = ValorPizzaFormSet(request.POST, instance=pizza)
        if form.is_valid() and formset.is_valid():
            form.save()
            formset.save()
            return redirect('pizzas:lista-pizzas')

def detalhe(request, pk):
    template_name = 'cadastro_pizza/detalhe-pizza.html'
    pizza = Pizza.objects.get(pk=pk)
    context = {}
    context['pizza'] = pizza
    return render(request, template_name, context)

def novo_ingrediente(request):
    template_name = 'cadastro_pizza/cadastro-ingrediente.html'
    context = {
        'form': CadastroIngredienteForm
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
