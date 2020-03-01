from django.shortcuts import render, redirect
from .models import Funcionarios

# Create your views here.
def home(req):
    return render(req, 'views/home.html')


def funcionarios(req):
       
    func = Funcionarios.objects.all()
    
    context = {
        'req': req,
        'func': func
    }

    return render(req, 'views/funcionarios/index.html',
                  context)
       
def cadastroFuncionario(req):
    
    context = {
        'req': req
    }
    
    return render(req, 
                 'views/funcionarios/cadastrar.html',
                 context )

def cadastrarFuncionario(req):
    
    newFunc = Funcionarios.objects.create(
                nome = req.POST['nome'],
                sobrenome = req.POST['sobrenome'],
                cargo = req.POST['cargo'],
                empresa = req.POST['empresa']
              )
    
    newFunc.save()
    
    return redirect('funcionarios')
    
def deletarFuncionario(req, id):
    
    existFunc = Funcionarios.objects.get(id=id)
    existFunc.delete()
    
    return redirect('funcionarios')
    
    

def editarFuncionario(req, id):
    
    funcionario = Funcionarios.objects.get(id=id)
    
    context = {
        'req': req,
        'func': funcionario
    }
    
    return render(req, 'views/funcionarios/editar.html', context)
    
def editado(req, id):
  
    func = Funcionarios.objects.get(id=id)
    func.nome = req.POST['nome']
    func.sobrenome = req.POST['sobrenome']
    func.empresa =req.POST['empresa']
    func.cargo = req.POST['cargo']
    func.save()
    
    
    return redirect('funcionarios')












 
    
    
