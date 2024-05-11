from django import forms
from .models import WasteOrder

class WasteOrderForm(forms.ModelForm):
    class Meta:
        model = WasteOrder
        fields = ['waste_type', 'bin_picture', 'size']