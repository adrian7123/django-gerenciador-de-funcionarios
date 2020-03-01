"""my_blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from my_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name="home"),
    path('funcionarios/', views.funcionarios, name="funcionarios"),
    
    path('funcionario/cadastro', views.cadastroFuncionario, name="cadastroFunc"),
    path('funcionario/cadastrar', views.cadastrarFuncionario, name="cadastrarFunc"),
    
    path('funcionario/deletar/<int:id>', views.deletarFuncionario, name="deletarFunc"),
    path('funcionario/editar/<int:id>', views.editarFuncionario, name="editarFunc"),  
    path('fufuncionario/editado/<int:id>', views.editado, name="editado" )
    
]
