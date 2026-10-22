import os
import random
import django

from datetime import date, timedelta, time

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from huellasSanas.models import Mascota, Cita


def generar_datos():
    nombres = [
        "Luna", "Max", "Bella", "Toby", "Milo",
        "Nala", "Rocky", "Kira", "Simba", "Coco",
        "Daisy", "Bruno", "Mia", "Thor", "Lola",
        "Leo", "Canela", "Bobby", "Kiara", "Tommy"
    ]

    especies = [
        "Perro", "Gato", "Conejo", "Hámster"
    ]

    razas = {
        "Perro": ["Labrador", "Poodle", "Pastor Alemán", "Mestizo", "Beagle"],
        "Gato": ["Siamés", "Persa", "Mestizo", "Bengalí", "Angora"],
        "Conejo": ["Cabeza de León", "Rex", "Holandés", "Enano"],
        "Hámster": ["Sirio", "Roborovski", "Chino"]
    }

    duenos = [
        "Ana González", "Carlos Muñoz", "María Rojas",
        "Pedro Silva", "Camila Torres", "Diego Soto",
        "Valentina Díaz", "Javier Pérez", "Sofía Castro",
        "Matías Morales", "Fernanda Reyes", "Andrés Flores",
        "Daniela Contreras", "Felipe Vargas", "Isidora Herrera",
        "Tomás Sepúlveda", "Antonia Fuentes", "Sebastián Espinoza",
        "Catalina Araya", "Nicolás Valdés"
    ]

    motivos = [
        "Control general",
        "Vacunación anual",
        "Consulta por pérdida de apetito",
        "Control de peso",
        "Problemas digestivos",
        "Revisión dermatológica",
        "Desparasitación",
        "Control dental",
        "Consulta por cojera",
        "Esterilización: evaluación previa"
    ]

    estados = ["pendiente", "atendida", "cancelada"]

    # Evitar duplicar los registros si se ejecuta más de una vez.
    if Mascota.objects.exists() or Cita.objects.exists():
        print("Ya existen mascotas o citas en la base de datos.")
        print("No se generaron nuevos registros.")
        print("Si deseas empezar de cero, elimina los datos de prueba primero.")
        return

    mascotas = []

    for i in range(20):
        especie = random.choice(especies)

        mascota = Mascota.objects.create(
            nombre=nombres[i],
            especie=especie,
            raza=random.choice(razas[especie]),
            dueño=duenos[i]
        )

        mascotas.append(mascota)

    hoy = date.today()

    for mascota in mascotas:
        fecha_cita = hoy + timedelta(days=random.randint(-15, 30))

        hora_cita = time(
            hour=random.choice([9, 10, 11, 12, 14, 15, 16, 17]),
            minute=random.choice([0, 15, 30, 45])
        )

        Cita.objects.create(
            mascota=mascota,
            fecha=fecha_cita,
            hora=hora_cita,
            motivo=random.choice(motivos)
        )

    print("¡Datos ficticios creados correctamente!")
    print(f"Mascotas creadas: {Mascota.objects.count()}")
    print(f"Citas creadas: {Cita.objects.count()}")


if __name__ == "__main__":
    generar_datos()