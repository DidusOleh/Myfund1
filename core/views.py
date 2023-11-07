from django.shortcuts import render, redirect
from item.models import Category, Item
from django.contrib.auth.decorators import login_required
from .forms import SignupForm, UserEditForm
from django.contrib.auth.models import User


def index(request):
    items = Item.objects.filter(is_over=False)[0:6]
    categories = Category.objects.all()
    return render(
        request,
        "core\index.html",
        {
            "categories": categories,
            "items": items,
        },
    )


def contact(request):
    return render(request, "core\contact.html")


def signup(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()

            return redirect("/login/")
    else:
        form = SignupForm()
    return render(request, "core/signup.html", {"form": form})

@login_required
def user(request, pk):
    user = User.objects.get(id=pk)
    if request.method == "POST":
        form = UserEditForm(request.POST,instance=user)
        if form.is_valid():
            form.save()

            return redirect("user/<int:pk>/")
    else:
        form = UserEditForm(instance=user)
    return render(request, "core/user.html",{'form': form})
