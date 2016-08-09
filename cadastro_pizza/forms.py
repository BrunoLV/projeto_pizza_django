from django import forms

class CadastroPizzaForm(forms.Form):
    sabor = forms.CharField(required=True)
    descricao = forms.CharField(required=True, widget=forms.Textarea)
    valor = forms.DecimalField(required=True)