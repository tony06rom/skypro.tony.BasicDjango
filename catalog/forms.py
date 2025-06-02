from django import forms
from django.core.exceptions import ValidationError
from django.db.models import BooleanField

from .models import Product


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for fild_name, fild in self.fields.items():
            if isinstance(fild, BooleanField):
                fild.widget.attrs['class'] = "form-check-input"
            else:
                fild.widget.attrs['class'] = "form-control"


class ProductForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'image', 'category', 'price']
        exclude = ['created_at', 'updated_at']

    FORBIDDEN_WORDS = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']

    def clean_name(self):
        name = self.cleaned_data.get('name')
        for word in self.FORBIDDEN_WORDS:
            if word in name.lower():
                raise ValidationError(f'Нельзя создать продукт, используя слова: {', '.join(self.FORBIDDEN_WORDS)}')
        return name

    def clean_description(self):
        description = self.cleaned_data.get('description')
        for word in self.FORBIDDEN_WORDS:
            if word in description.lower():
                raise ValidationError(f'Найдено запрещенное слово в описании: {self.FORBIDDEN_WORDS}')
        return description

    def clean_price(self):
        price = self.cleaned_data.get('price')
        if price <= 0:
            raise ValidationError('Цена не может быть отрицательной или ровняться нулю')
        return price
