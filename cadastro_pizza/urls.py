from django.conf.urls import url

from cadastro_pizza.views import CadastroIngredienteView, PizzaCreate, PizzaUpdate, PizzaDelete
from . import views

urlpatterns = [
    url(r'^$', views.index, name = 'index'),
    url(r'^ingredientes/cadastrar$', CadastroIngredienteView.as_view(), name='cadastra-ingrediente'),
    url(r'^pizzas/cadastrar/$', PizzaCreate.as_view(), name='cadastra-pizza'),
    url(r'^pizzas/(?P<pk>[0-9]+)/edit/$', PizzaUpdate.as_view(), name='edita-pizza'),
    url(r'^pizzas/(?P<pk>[0-9]+)/delete/$', PizzaDelete.as_view(), name="exclui-pizza"),
    url(r'^pizzas/listar$', views.lista_pizzas, name='lista-pizzas'),

]