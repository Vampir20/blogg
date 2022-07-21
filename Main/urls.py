from django.urls import path
from Main.views import main_page, login, register, profile, log_out

urlpatterns = [
    path('', main_page, name='main_page'),
    path('login/', login, name='login'),
    path('register/', register, name='register'),
    path('profile/', profile, name='profile'),
    path('logout/', log_out, name='logout')
]