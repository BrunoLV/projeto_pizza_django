from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import ListView
from django.views.generic.edit import View, CreateView, UpdateView, DeleteView, ModelFormMixin
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
    context = {
        'form':CadastroPizzaForm
    }
    if request.method == 'GET':
        return render(request, template_name, context)
    if request.method == 'POST':
        form = CadastroPizzaForm(request.POST)
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