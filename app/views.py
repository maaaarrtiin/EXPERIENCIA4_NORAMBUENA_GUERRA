from django.shortcuts import redirect, render
from django.views.decorators import csrf
from .models import Cliente,Producto
from .forms import ClienteForm,ProductoForm

def index(request):
    return render (request, 'index.html')

def quienessomos(request):
    return render(request, 'quienessomos.html')

def galeria(request):
    return render(request, 'galeria.html')

def formulario(request):
    return render (request, 'formulario.html')

def apiferiados(request):
    return render(request, 'apiferiados.html')

def mensaje(request):
    return render(request, 'mensaje.html')

def mostrar(request):
    clientes= Cliente.objects.all()
    datos={
        'clientes': clientes
    }
    return render(request, 'mostrar.html',datos)

def mostrar2(request):
    productos= Producto.objects.all()
    datos={
        'productos': productos
    }
    return render(request, 'mostrar2.html',datos)

def forms_clientes(request):
    if request.method=='POST':
        cliente_form = ClienteForm(request.POST)
        if cliente_form.is_valid():
            cliente_form.save()
            return redirect('mostrar')
    else:
        cliente_form= ClienteForm()
    return render(request, 'forms_clientes.html', {'cliente_form': cliente_form})


def form_mod_cliente(request, id):
    cliente = Cliente.objects.get(rut=id)
    datos ={
        'form': ClienteForm(instance=cliente)
    }
    if request.method=='POST':
        formulario = ClienteForm(data = request.POST, instance=cliente)
        if formulario.is_valid: 
            formulario.save()
            return redirect('mostrar')
    return render(request, 'form_mod_cliente.html', datos)


def form_del_cliente(request, id):
    cliente = Cliente.objects.get(rut=id)
    cliente.delete()
    return redirect('mostrar')

def forms_productos(request):
    if request.method=='POST':
        producto_form = ProductoForm(request.POST, files=request.FILES)
        if producto_form.is_valid():
            producto_form.save()
            return redirect('mostrar2')
    else:
        producto_form= ProductoForm()
    return render(request, 'forms_productos.html', {'producto_form': producto_form})


def form_mod_producto(request, id):
    producto = Producto.objects.get(idprod=id)
    datos ={
        'form': ProductoForm(instance=producto)
    }
    if request.method=='POST':
        formulario = ProductoForm(data = request.POST, files=request.FILES,instance=producto)
        if formulario.is_valid: 
            formulario.save()
            return redirect('mostrar2')
    return render(request, 'form_mod_producto.html', datos)

def form_del_producto(request, id):
    producto = Producto.objects.get(idprod=id)
    producto.delete()
    return redirect('mostrar2')

# Create your views here.
