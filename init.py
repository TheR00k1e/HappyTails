import os
import django
from datetime import datetime 

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'happytails.settings')
django.setup()

from main.models import * 


#Poblar modelo EstadoCivil
def crear_estadocivil():

    tipo_estado_civil = ['Soltero', 'Casado', 'Viudo']

    for i in tipo_estado_civil:
        cat_obj,_ = EstadoCivil.objects.get_or_create(tipo_estado_civil=i)
        cat_obj.save()


#Poblar modelo Especialidad
def crear_especialidad():

    nombre_especialidad = ['Canina', 'Felina', 'Aviar']

    for i in nombre_especialidad:
        cat_obj,_ = Especialidad.objects.get_or_create(nombre_especialidad=i)
        cat_obj.save()

#Poblar modelo RazaPaciente
def crear_razapaciente():

    raza_perro = ['Pastor alemán', 'Bulldog', 'Labrador retriever', 'Golden retriever', 'Bulldog francés', 'Husky siberiano', 'Beagle',
                   'Poodle', 'Chihuahua', 'Rottweiler', 'Chow Chow', 'Bóxer', 'Doberman'] 
    
    raza_gato = ['Siamés', 'Persa', 'Esfinge', 'Siberiano', 'Birmano', 'Fold escocés', 'Burmés']       

    raza_ave = ['Agapornis', 'Amazona aestiva', 'Cacatúa', 'Canarios', 'Cotorra alejandrina', 'Diamante mandarín', 'Guacamayos',
                'Ninfas', 'Periquitos', 'Pinzones']
    
    for raza in raza_perro:
        RazaPaciente.objects.get_or_create(raza_paciente='perro', raza_perro=raza)

    for raza in raza_gato:
        RazaPaciente.objects.get_or_create(raza_paciente='gato', raza_gato=raza)

    for raza in raza_ave: 
        RazaPaciente.objects.get_or_create(raza_paciente='ave', raza_ave=raza)  


#Poblar modelo TipoPaciente
def crear_tipopaciente():

    tipo_paciente = ['Perro', 'Gato', 'Ave']

    # Obtener un objeto RazaPaciente existente (por ejemplo, el primero)
    raza_paciente = RazaPaciente.objects.first()

    if raza_paciente:
        for tipo in tipo_paciente:
            TipoPaciente.objects.get_or_create(raza_paciente=raza_paciente, tipo_paciente=tipo)    


#Poblar modelo Tratamiento
def crear_tipotratamiento():

    tipo_tratamiento = ['Cirugía', 'Dietoterapia', 'Farmacoterapia', 'Fisioterapia', 'Hidroterapia', 'Prótesis']

    for i in tipo_tratamiento:
        cat_obj,_ = Tratamiento.objects.get_or_create(tipo_tratamiento=i)
        cat_obj.save()     





if __name__ == '__main__':
    print("Creando registros en la BBD para EstadoCivil")
    crear_estadocivil()

if __name__ == '__main__':
    print("Creando registros en la BBDD para Especialidad")
    crear_especialidad()

if __name__ == '__main__':
    print("Creando registros en la BBDD para RazaPaciente ")   
    crear_razapaciente()

if __name__ == '__main__':
    print("Creando registros en la BBDD para TipoPaciente")
    crear_tipopaciente()

if __name__ == '__main__':
    print("Creando registros en la BBDD para Tratamiento")
    crear_tipotratamiento()    