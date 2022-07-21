from django.shortcuts import render, redirect
from Articles.models import Article
from Main.models import Author
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login as django_login
from django.contrib.auth import logout
from django.contrib import messages


def main_page(request):
    first_article = Article.objects.all().first()
    print(first_article)
    if request.session.get('login'):
        message = "Авторизация прошла успешно"
        del request.session['login']
    if request.session.get('logout'):
        message = "Вы успешно вышли из системы"
        del request.session['logout']
    return render(request, 'Main/main_page.html', locals())


def login(request):
    if request.method == 'POST':
        user_username = request.POST.get('nickname')
        user_password = request.POST.get('password')
        user = authenticate(username=user_username, password=user_password)
        if user:
            django_login(request, user)
            request.session['login'] = True
            return redirect('main_page')
        else:
            messages.error(request, "Введенные данные не верны")
    return render(request, 'Main/login.html')


def register(request):
    if request.method == 'POST':
        user_username = request.POST.get('nickname')
        user_email = request.POST.get('email')
        user_password = request.POST.get('password1')
        user_password_two = request.POST.get('password2')
        if user_password != user_password_two:
            messages.error(request, 'пароли не совпадают')
        if User.objects.filter(username=user_username).exists():
            messages.error(request, 'такой username уже занят')
        if User.objects.filter(email=user_email).exists():
            messages.error(request, 'такой Email уже занят')
        if not messages:
            new_user = User.objects.create_user(username=user_username, email=user_email, password=user_password)
            new_user.save()
    return render(request, 'Main/register.html')


def log_out(request):
    logout(request)
    request.session["logout"] = True
    return redirect("main_page")


def profile(request):
    if request.user.is_authenticated:
        author = Author.objects.get(username_id=request.user.id)
        if request.method == "POST":
            author = Author.objects.get(username_id=request.user.id)
            # update_user = User.objects.get(id=author.id)
            # данные ключа которые мы кладем в обект
            author.username.username = request.POST["username"]
            author.username.email = request.POST["email"]
            author.username.save()
        return render(request, 'Main/profile.html', locals())
    else:
        return redirect("register")

def handler_404(request, exception):
    return redirect("main_page")