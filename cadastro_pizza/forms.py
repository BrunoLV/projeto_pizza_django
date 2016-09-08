from django.forms import ModelForm, Textarea, TextInput, NumberInput, CheckboxSelectMultiple
from django.utils.translation import ugettext_lazy as _
from .models import Pizza, Ingrediente

class CadastroPizzaForm(ModelForm):
    
    class Meta:
        model = Pizza
        fields = '__all__'
        labels = {
            'sabor': _('Sabor:'),
            'descricao': _('Descrição:'),
            'ingredientes': _('Ingredientes:')
        }
        widgets = {
            'sabor': TextInput(attrs={'class':'form-control'}),
            'descricao': Textarea(attrs={'rows':'5', 'class':'form-control'}),
            'ingredientes': CheckboxSelectMultiple(),
        }

class CadastroIngredienteForm(ModelForm):

	class Meta:
		model = Ingrediente
		fields = ['nome', 'descricao']
		widgets = {
			'nome': TextInput(attrs={'class':'form-control'}),
			'descricao':Textarea(attrs={'rows':'5', 'class':'form-control'})
		}
