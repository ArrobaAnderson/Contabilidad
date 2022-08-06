from django.shortcuts import render

# Create your views here.

def inicio(request):
    data = {
        'titulo':"Inicio"
    }
    return render(request,'base.html',data)

def contabilidad(request):
  data = {
        'titulo': "Inicio"
  }
  return render(request, "contabilidad/contabilidad.html",data)

def ejercicio(request):
    data = {
        'titulo': 'DATOS DE EJERCICIO',
        'crear_url': '/crearejercicio',
        'listar_url': '/ejercicio',
    }
    return render(request, "contabilidad/Ejercicio/ejercicio.html", data)

def crearejercicio(request):
    data = {
        'titulo': 'CREACION DE EJERCICIO',
        'action': 'add',
        'listar_url': '/ejercicio',
    }
    return render(request, "contabilidad/Ejercicio/crearEjercicio.html", data)

def libromayor(request):
    data = {
        'titulo': 'DATOS DE MAYOR',
        'crear_url': '/crearmayor',
        'listar_url': '/libromayor',
    }
    return render(request, "contabilidad/libromayor/libromayor.html", data)

def crearmayor(request):
    data = {
        'titulo': 'CREACION DE MAYOR',
        'action': 'add',
        'listar_url': '/libromayor',
    }
    return render(request, "contabilidad/libromayor/crearMayor.html", data)

def detmayor(request):
    data = {
        'titulo': 'DATOS DE MAYOR',
        'crear_url': '/crearmayor',
        'listar_url': '/libromayor',
    }
    return render(request, "contabilidad/libromayor/detMayor.html", data)

def diario(request):
    data = {
        'titulo': 'GESTION DE DIARIO',
        'crear_url': '/creardiario',
        'listar_url': '/diario',
    }
    return render(request, "contabilidad/Diario/diario.html", data)

def creardiario(request):
    data = {
        'titulo': 'CREACION DE DIARIO',
        'action': 'add',
        'listar_url': '/diario',
    }
    return render(request, "contabilidad/Diario/crearDiario.html", data)

def detdiario(request):
    data = {
        'titulo': 'GESTION DE DIARIO',
        'crear_url': '/creardiario',
        'listar_url': '/diario',
    }
    return render(request, "contabilidad/Diario/detDiario.html", data)



def articulo(request):
  return HttpResponse(html_base+
    """<h2>Mantenimiento de Articulo</h2>
       <p>List de articulos</p>""")

def cliente(request):
  data = {
      'titulo':'GESTION DE CLIENTESssss',
      'crear_url': '/crearcliente',
      'listar_url': '/cliente',
  }
  return render(request, "ventas/clientes/listCliente.html",data)

def crearCliente(request):
  data = {
      'titulo':'MANTENIMIENTO DE CLIENTES',
      'crear_url':'/crearcliente',
      'action':'add',
      'listar_url': '/cliente',
  }
  return render(request, "ventas/clientes/formCliente.html",data)

def venta(request):
  data = {
        'titulo': "Inicio"
  }
  return render(request, "ventas/ventas.html",data)