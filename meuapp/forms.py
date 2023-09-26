from django import forms


class AddListaOrd(forms.Form):
    nome = forms.CharField(max_length=25)
    nutriente = forms.CharField(max_length=25)
    cor = forms.CharField(max_length=25)
