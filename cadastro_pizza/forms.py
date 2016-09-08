from django.forms import ModelForm, Textarea, TextInput, NumberInput, CheckboxSelectMultiple
from .models import Pizza, Ingrediente

class CadastroPizzaForm(ModelForm):
    
    class Meta:
        model = Pizza
        fields = ['sabor', 'descricao', 'ingredientes']
        widgets = {
            'sabor': TextInput(attrs={'class':'form-control'}),
            'descricao': Textarea(attrs={'rows':'5', 'class':'form-control'}),
            'ingredientes': CheckboxSelectMultiple(attrs={'class':'form-control'}),
        }

class CadastroIngredienteForm(ModelForm):

	class Meta:
		model = Ingrediente
		fields = ['nome', 'descricao']
		widgets = {
			'nome': TextInput(attrs={'class':'form-control'}),
			'descricao':Textarea(attrs={'rows':'5', 'class':'form-control'})
		}
