from django import forms
from .models import Product

class ProductForm(forms.Form):
    name = forms.CharField(max_length=200, label='Nombre')
    description = forms.CharField(max_length=500, label='Descripcion', widget=forms.Textarea)
    price = forms.DecimalField(max_digits=10, decimal_places=2, label='Precio')
    available = forms.BooleanField(required=False, label='Disponible')
    photo = forms.ImageField(required=False, label='Foto')

    def save(self):
        data = self.cleaned_data
        product = Product(
            name=data['name'],
            description=data['description'],
            price=data['price'],
            available=data['available'],
            photo=data['photo']
        )

        product.save()
    
