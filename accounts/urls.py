
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('autenticar/', views.autenticar, name='autenticar'),
    path('cadastrar/', views.cadastrar, name='cadastrar'),
    path('cadastro/', views.cadastro, name='cadastro'),
    path('user/exist', views.user_exist, name='user_exist'),
    path('user/', views.user, name='user'),
    path('publicar/', views.publicar, name='publicar'),
    path('user/post/<int:post_id>', views.detail, name='detail'),
    path('user/logout', views.logoff, name='logout'),
]
