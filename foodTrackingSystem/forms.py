from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    """ def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)
        self.fields['code'].disabled = True """

    class Meta:
        model = Product
        fields = ('code',)

""" class DetailForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        # super(DetailForm, self).__init__(*args, **kwargs)
        self.fields['code'].disabled = True

    class Meta:
        model = Product
        fields = ['code']
        lables = {'code': ('cieo')} """