from django.conf.urls import url

from cadastro_pizza.views import PizzaDelete
from . import views

urlpatterns = [
    url(r'^$', views.index, name = 'index'),
    url(r'^pizzas/(?P<pk>[0-9]+)/edit/$', views.edita_pizza, name='edita-pizza'),
    url(r'^pizzas/(?P<pk>[0-9]+)/delete/$', PizzaDelete.as_view(), name="exclui-pizza"),
    url(r'^pizzas/listar$', views.lista_pizzas, name='lista-pizzas'),
    url(r'^pizzas/nova/$', views.nova_pizza, name='nova-pizza'),
    url(r'^pizzas/cardapio/$', views.cardapio, name='cardapio'),
    url(r'^ingredientes/novo/$', views.novo_ingrediente, name='novo-ingrediente'),
]
