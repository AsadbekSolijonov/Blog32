from django.http import HttpResponse
from django.shortcuts import render, redirect

from account.forms import CustomUserCreationForm


def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = CustomUserCreationForm()

    context = {
        "form": form
    }
    return render(request, 'account/register.html', context=context)
