from django import forms
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User

class UserEditForm(UserChangeForm):
    class Meta:
        model = User
        fields = ("username", "email", "last_name", "first_name")
    
    
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Your username",
                "class": "w-full rounded-full placeholder:italic placeholder:text-slate-400  bg-white border border-slate-300 py-2 pl-9 pr-3 shadow-sm focus:outline-none focus:border-sky-500 focus:ring-sky-500 focus:ring-1",
            }
        )
    )

    email = forms.CharField(
        widget=forms.EmailInput(
            attrs={
                "placeholder": "Your email address",
                "class": "w-full rounded-full placeholder:italic placeholder:text-slate-400  bg-white border border-slate-300 py-2 pl-9 pr-3 shadow-sm focus:outline-none focus:border-sky-500 focus:ring-sky-500 focus:ring-1",
            }
        )
    )

    first_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Your name",
                "class": "w-full rounded-full placeholder:italic placeholder:text-slate-400  bg-white border border-slate-300 py-2 pl-9 pr-3 shadow-sm focus:outline-none focus:border-sky-500 focus:ring-sky-500 focus:ring-1",
            }
        )
    )

    last_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Your surname",
                "class": "w-full rounded-full placeholder:italic placeholder:text-slate-400  bg-white border border-slate-300 py-2 pl-9 pr-3 shadow-sm focus:outline-none focus:border-sky-500 focus:ring-sky-500 focus:ring-1",
            }
        )
    )