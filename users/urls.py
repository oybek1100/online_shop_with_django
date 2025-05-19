from django.urls import path
from .views import login_page

app_name = 'users'

urlpatterns = [
    path('login/', login_page, name='login'),
]