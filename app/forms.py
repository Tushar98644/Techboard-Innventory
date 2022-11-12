from django import forms
from .models import Inventory,Book
class InventoryForm(forms.ModelForm):
    class Meta:
        model = Inventory
        fields = ('product','price','Quantity')
class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ('ClubName','Intime','Outtime')