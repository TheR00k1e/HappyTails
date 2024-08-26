import os
import django
import json
from datetime import datetime 

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'happytails.settings')
django.setup()

from main.models import * 

def load_regions():
    with open('D:/Happytails/regiones.json', encoding='utf-8') as f:
        data = json.load(f)
        for item in data:
            Region.objects.get_or_create(
                codigo=item['codigo'],
                tipo=item['tipo'],
                nombre=item['nombre'],
                lat=item['lat'],
                lng=item['lng'],
                url=item['url']
            )

def load_provincias():
    with open('D:/Happytails/provincias.json', encoding='utf-8') as f:
        data = json.load(f)
        for item in data:
            region_codigo = item['codigo_padre']
            region = Region.objects.get(codigo=region_codigo)
            Provincia.objects.get_or_create(
                codigo=item['codigo'],
                tipo=item['tipo'],
                nombre=item['nombre'],
                lat=item['lat'],
                lng=item['lng'],
                url=item['url'],
                codigo_padre=item['codigo_padre'],
                region=region
            )
def load_comunas():
    with open('D:/Happytails/comunas.json', encoding='utf-8') as f:
        data = json.load(f)
        for item in data:
            provincia_codigo = item['codigo_padre']
            provincia = Provincia.objects.get(codigo=provincia_codigo)
            Comuna.objects.get_or_create(
                codigo=item['codigo'],
                tipo=item['tipo'],
                nombre=item['nombre'],
                lat=item['lat'],
                lng=item['lng'],
                url=item['url'],
                codigo_padre=item['codigo_padre'],
                provincia=provincia
            )

if __name__ == '__main__':
    print("Cargando datos en la BDD para Region")
    load_regions()

if __name__ == '__main__':
    print("Cargando datos en la BDD para Provincia")
    load_provincias()

if __name__ == '__main__':
    print("Cargando datos en la BDD para Comuna")
    load_comunas()