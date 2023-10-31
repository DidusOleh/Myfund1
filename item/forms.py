from django import forms

from .models import Item

INPUT_CLASSES = "w-full py-4 px-6 rounded-xl border"


class NewItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ("category", "name", "description", "donation", "image")
        widgets = {
            "category": forms.Select(attrs={"class": INPUT_CLASSES}),
            "name": forms.TextInput(attrs={"class": INPUT_CLASSES}),
            "descrition": forms.Textarea(attrs={"class": INPUT_CLASSES}),
            "donation": forms.NumberInput(attrs={"class": INPUT_CLASSES}),
            "image": forms.FileInput(attrs={"class": INPUT_CLASSES}),
        }


class EditItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ("name", "description", "donation", "image", "is_over")
        widgets = {
            "name": forms.TextInput(attrs={"class": INPUT_CLASSES}),
            "descrition": forms.Textarea(attrs={"class": INPUT_CLASSES}),
            "donation": forms.NumberInput(attrs={"class": INPUT_CLASSES}),
            "image": forms.FileInput(attrs={"class": INPUT_CLASSES}),
        }
