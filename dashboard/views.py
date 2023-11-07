from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from item.models import Item
from django.contrib.auth.models import User
from .forms import UserEditForm


@login_required
def index(request):
    items = Item.objects.filter(created_by=request.user)

    return render(
        request,
        "dashboard/index.html",
        {
            "items": items,
        },
    )

@login_required
def userEdit(request, pk):
    user = User.objects.get(id=pk)
    if request.method == "POST":
        form = UserEditForm(request.POST,instance=user)
        if form.is_valid():
            form.save()

            return redirect("dashboard:index")
    else:
        form = UserEditForm(instance=user)
    return render(request, "dashboard/edit.html",{'form': form})