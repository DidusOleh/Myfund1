from django import forms

from .models import Item

INPUT_CLASSES = "w-full rounded-full placeholder:italic placeholder:text-slate-400 bg-lime-300 py-2 pl-9 pr-3 shadow-sm focus:outline-none focus:border-sky-500 focus:ring-sky-500 focus:ring-1 text-black"


class NewItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ("category", "name", "description", "donation", "image")
        widgets = {
            "category": forms.Select(attrs={"class": INPUT_CLASSES}),
            "name": forms.TextInput(attrs={"class": INPUT_CLASSES}),
            "description": forms.Textarea(attrs={"class": INPUT_CLASSES, "style": "border-radius: 0;"}),
            "donation": forms.NumberInput(attrs={"class": INPUT_CLASSES}),
            "image": forms.FileInput(attrs={"class": INPUT_CLASSES}),
        }


class EditItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ("name", "description", "donation", "image", "is_over")
        widgets = {
            "name": forms.TextInput(attrs={"class": INPUT_CLASSES}),
            "description": forms.Textarea(attrs={"class": INPUT_CLASSES, "style": "border-radius: 0;"}),
            "donation": forms.NumberInput(attrs={"class": INPUT_CLASSES}),
            "image": forms.FileInput(attrs={"class": INPUT_CLASSES}),
        }
