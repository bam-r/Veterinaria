from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import Cita, Mascota

def inicio(request):
    return render(request, 'gestion/inicio.html')

def obtener_citas(request):
    citas = list( Cita.objects.values())
    
    return JsonResponse(citas, safe=False)

def obtener_mascotas(request):
    mascotas = list( Mascota.objects.values())
    
    return JsonResponse(mascotas, safe=False)

def mascotas_agregar(request):
    if request.method == 'POST':
        nombre= request.POST.get('nombre')
        especie= request.POST.get('especie')
        raza= request.POST.get('raza')
        dueño= request.POST.get('dueño')
        
        Mascota.objetcs.create(
            nombre=nombre,
            especie=especie,
            raza=raza,
            dueño=dueño
        )
        
        return redirect('inicio')

def citas_agregar(request):
    if request.method == 'POST':
        fecha= request.POST.get('fecha')
        hora= request.POST.get('hora')
        motivo= request.POST.get('motivo')
        mascota_id = request.POST.get('mascota')
        mascota = Mascota.objects.get(pk=mascota_id)
        
        Cita.objects.create(
            fecha=fecha,
            hora=hora,
            motivo=motivo,
            mascota=mascota
        )

        return redirect('inicio')
    mascotas = Mascota.objects.all()

    return render(
        request,
        'gestion/citas_agregar.html',
        {'mascotas': mascotas}
    )