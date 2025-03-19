from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login as login_django, logout as logout_django
from django.contrib.auth import get_user_model

User = get_user_model()

def index(request):
    return redirect("book")

def login(request):
    if request.user.is_authenticated:
        return redirect("/")
    return render(request, "login.html")

def auth_login(request):
    if not request.method == "POST":
        messages.error(request, "Metodo não permitido!")
        return redirect("login")
    post = request.POST
    email = post.get("email")
    password = post.get("password")
    user = authenticate(request, username=email, password=password)
    if user is not None:
        login_django(request, user)
        return redirect("/")
    else:
        messages.error(request, "Usuário ou senha incorretas!")
        return redirect("login")
    

def auth_register(request):
    if request.method != "POST":
        messages.error(request, "Método não permitido!")
        return redirect("login")

    post = request.POST
    name = post.get("name")
    last_name = post.get("last_name")
    email = post.get("email")
    password = post.get("password")
    password_confirm = post.get("password_confirm")

    # Verifica se já existe um usuário com esse email
    if User.objects.filter(username=email).exists():
        messages.error(request, "Este e-mail já está cadastrado!")
        return redirect("register")

    if password != password_confirm:
        messages.error(request, "As senhas não coincidem!")
        return redirect("register")

    user = User.objects.create_user(
        username=email,
        email=email,
        password=password,
        first_name=name,
        last_name=last_name
    )
    user.backend = "django.contrib.auth.backends.ModelBackend"
    login_django(request, user)

    return redirect("sobre")

def logout(request):
    logout_django(request)
    return redirect("login")

def register(request):
    return render(request, "register.html")


def sobre(request, disabled=False):
    return render(request, "sobre.html", context={'disabled': disabled})