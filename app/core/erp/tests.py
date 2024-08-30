# from django.test import TestCase

# Create your tests here.

# from config.wsgi import *
# from core.erp.models import Type, Employee

# Listar

# select * from tabla

# query = Type.objects.all()
# print(query)

# Inserción
# t = Type(name = 'Administrador').save()
# t = Type(name = 'Administrador')
# t = Type()
# t.name = 'Vendedor'
# t.save()

# Edición
# try:
#     t = Type.objects.get(id = 1)
#     # t = Type.objects.get(pk = 1)
#     t.name = 'Contador'
#     t.save()
# except Exception as e:
#     print(e)

# Eliminación
# t = Type.objects.get(pk = 1)
# t.delete()

# Listar mediante filtros
# obj = Type.objects.filter(name__contains = 'Pre')
# obj = Type.objects.filter(name__icontains = 'pre')
# obj = Type.objects.filter(name__startswith = 'P')
# obj = Type.objects.filter(name__endswith = 'r')
# obj = Type.objects.filter(name__in = ['Vendedor', 'Conductor']).count()
# obj = Type.objects.filter(name__contains = 'Pre').query
# obj = Type.objects.filter(name__endswith = 'r').exclude(id = 5)

# obj = Employee.objects.filter(type_id = 1)
#
# for i in Type.objects.filter(name__endswith = 'r')[:2]:
#     print(i.name)