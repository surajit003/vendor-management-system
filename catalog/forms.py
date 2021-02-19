from django import forms
from .models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        exclude = (
            "created_by",
            "slug",
        )
        labels = {
            "image_one": "ProductImage1",
            "image_two": "ProductImage2",
            "image_three": "ProductImage3",
            "image_four": "ProductImage4",
            "image_five": "ProductImage5",
        }

        def clean_price(self):
            if self.cleaned_data["price"] <= 0:
                raise forms.ValidationError("Price must be greater than zero.")
            return self.cleaned_data["price"]
