from django.shortcuts import render
from .models import TipoIA, Concepto, Infografia


def inicio(request):
    tipos = TipoIA.objects.all()
    conceptos = Concepto.objects.all()
    infografias = Infografia.objects.all()

    return render(request, 'principal/inicio.html', {
        'tipos': tipos,
        'conceptos': conceptos,
        'infografias': infografias,
    })


def ia(request):
    tipos = TipoIA.objects.all()

    return render(request, 'principal/ia.html', {
        'tipos': tipos
    })

def linea_tiempo(request):
    return render(request, 'principal/linea_del_tiempo.html')

def infografias(request):
    infografias = Infografia.objects.all()
    return render(request, 'principal/infografias.html', {
        'infografias': infografias
    })

def conceptos(request):
    conceptos = Concepto.objects.all()

    return render(request, 'principal/conceptos.html', {
        'conceptos': conceptos
    })