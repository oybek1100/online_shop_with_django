from django.shortcuts import render

# Create your views here.

def login_page(reques):
    return render(reques, 'users/login.html')
