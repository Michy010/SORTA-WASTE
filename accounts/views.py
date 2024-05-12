from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from . forms import CustomUserForm
from django.contrib.auth.models import Group


# Create your views here.
def signup (request):
    if request.method == 'POST':
        form = CustomUserForm (request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_seller = form.cleaned_data['is_seller']
            user.save()
            if user.is_seller:
                seller_group, _ = Group.objects.get_or_create(name='Seller')
                user.groups.add(seller_group)
            return redirect('accounts:login')
    else:
        form = CustomUserForm()
    return render(request, 'accounts/signup.html', {'form': form})

def signin (request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('sorta_Waste:orders')
        else:
            messages.error(request, 'password or username is incorrect')

    return render (request, 'accounts/signin.html')