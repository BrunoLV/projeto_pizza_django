from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import ListView
from django.views.generic.edit import View, CreateView, UpdateView, DeleteView, ModelFormMixin
from django.core.urlresolvers import reverse_lazy

from .models import Pizza, Ingrediente, IngredientesPizza
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

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.save()
        for ingrediente in form.cleaned_data['ingredientes']:
            ingredientes_pizza = IngredientesPizza()
            ingredientes_pizza.pizza = self.object
            ingredientes_pizza.ingrediente = ingrediente
            ingredientes_pizza.save()
        return super(ModelFormMixin, self).form_valid(form)

class PizzaUpdate(UpdateView):
    model = Pizza
    template_name_suffix = '_update_form'
    form_class = CadastroPizzaForm

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.save()
        for ingrediente in form.cleaned_data['ingredientes']:
            ingredientes_pizza = IngredientesPizza()
            ingredientes_pizza.pizza = self.object
            ingredientes_pizza.ingrediente = ingrediente
            ingredientes_pizza.save()
        return super(ModelFormMixin, self).form_valid(form)

class PizzaDelete(DeleteView):
    model = Pizza
    success_url = reverse_lazy('lista-pizzas')

class CadastroIngredienteView(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse('Testando get')

    def post(self, *args, **kwargs):
        return HttpResponse('Testando post')