from django.shortcuts import render, redirect

from django.contrib.auth import authenticate, login, logout

from django.contrib.auth.models import User

from django.http import HttpResponse

from .models import Post

from django.contrib.auth.decorators import login_required

# Create your views here.

def index(request):
    return render(request, 'accounts/index.html')

def autenticar(request):
    username = request.POST["username"]
    password = request.POST["userpassword"]

    user = authenticate(username=username, password=password)

    if user is not None:
        login(request, user)
        return redirect('user')
    else:
        return render(request, 'accounts/no_user.html')

def cadastrar(request):
    username = request.POST["username"]
    password = request.POST["userpassword"]
    user = authenticate(username=username, password=password)

    if user is not None:
        return render(request, 'accounts/user_exist.html')
    else:
        try:
            User.objects.create_user(username=username, password=password)
            return redirect('index')
        except:
            return render(request, 'accounts/user_exist.html')


def cadastro(request):
    return render(request, 'accounts/cadastro.html')

def user_exist(request):
    return render(request, 'accounts/user_exist.html')

@login_required()
def user(request):
    user = request.user
    posts = user.post_set.all()
    context = {
        'posts': posts
    }
    return render(request, 'accounts/user.html', context=context)
        
@login_required()
def publicar(request):
    titulo = request.POST['titulo']
    texto = request.POST['texto']
    user = request.user
    post = Post(author=user, title=titulo, content=texto)
    post.save()
    return redirect('user')

@login_required()
def detail(request, post_id):
    user = request.user
    post = user.post_set.get(id=post_id)
    context = {
        'post': post,
    }
    return render(request, 'accounts/detail.html', context=context)

def logoff(request):
    logout(request)
    return redirect('index')
