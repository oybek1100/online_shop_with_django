from django.shortcuts import render , redirect
from .forms import LoginForm
from django.contrib.auth import authenticate , login , logout
from django.contrib import messages
from django.contrib.auth import logout as django_logout  

# Create your views here.

def login_page(request):
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, username=cd['email'], password=cd['password'])
            if user:
                login(request, user)
                return redirect('shop:index')
            else:
                messages.add_message(
                    request,
                    messages.ERROR,
                    'Email yoki parol xato'
                )
    return render(request, 'users/login.html', {'form': form})






def logout_view(request):
    if request.method == 'POST':
        django_logout(request)
        return redirect('shop:index')
    

def register(request):
    return render(request, 'users/register.html')

