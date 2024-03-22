from rest_framework import serializers
from .models import *


class DocenteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Docente

        exclude = ['groups', 'user_permissions', 'last_login']
        # https://www.django-rest-framework.org/api-guide/serializers/#additional-keyword-arguments
        # podemos indicar que atributos o columnas de la tabla son solo escritura o solo lectura
        extra_kwargs = {
            'password': {
                'write_only': True
            },
            'is_staff': {
                'read_only': True
            },
            'is_active': {
                'write_only': True
            }
        }


class EstudianteSerializer(serializers.ModelSerializer):
    class Meta:

        model = Estudiante
        
        fields = '__all__'
        
class CursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Curso

        fields = '__all__'

class CursoEstudianteSerializer(serializers.ModelSerializer):
    class Meta:
        model = CursoEstudiante
        fields = '__all__'

class CalificacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Calificacion

        fields = '__all__'


class PromedioCalificacionCursos(serializers.ModelSerializer):
    cursoId = CursoSerializer()
    class Meta:                         
        model= Calificacion
        fields = '__all__'

                