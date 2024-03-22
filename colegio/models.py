from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager

class ManejadorUsuario(BaseUserManager):
    def create_superuser(self, nombre, correo, password):
        if not correo:
            raise ValueError('El usuario tiene que tener un correo')

        

        correo_normalizado = self.normalize_email(correo)

        nuevo_usuario = self.model(correo=correo_normalizado, nombre=nombre)
        
        nuevo_usuario.set_password(password)

        nuevo_usuario.is_superuser = True
        nuevo_usuario.is_staff = True

        nuevo_usuario.save()

class Docente(AbstractBaseUser, PermissionsMixin):
    id = models.AutoField(primary_key=True, unique=True, null=False)
    nombre = models.TextField(null=False)
    apellido = models.TextField(null=False)
    correo = models.EmailField(null=False, unique=True)
    password = models.TextField(null=False)
    especializacion = models.TextField(null=False)
    telefono = models.TextField(null=False)
    foto = models.ImageField(null=False)
    is_staff = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='docentes_groups',
        
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='docentes_user_permissions',

    )

    USERNAME_FIELD = 'correo'
    REQUIRED_FIELDS = ['nombre']

    objects = ManejadorUsuario()

    class Meta:
        db_table = 'docentes'



class Estudiante(models.Model):
    id = models.AutoField(primary_key=True, unique=True, null=False)
    nombre = models.TextField(null=False) 
    apellido = models.TextField(null=False)
    correo = models.EmailField(null=False, unique=True)
    password = models.TextField(null=False)
    foto = models.ImageField(null=False)

    class Meta:
        db_table = 'estudiantes'

class Curso(models.Model):
    id = models.AutoField(primary_key=True, unique=True, null=False)
    nombre = models.TextField(null=False)
    seccion = models.TextField(null=False)
    hInicio = models.TimeField(db_column='h_inicio',null=False)
    hFinal = models.TimeField(db_column='h_final', null=False)
    docenteId = models.ForeignKey(to=Docente, db_column='docente_id',on_delete=models.CASCADE, related_name='cursos')

    class Meta:
        db_table = 'cursos'

class CursoEstudiante(models.Model):
    id = models.AutoField(primary_key=True, unique=True, null=False)
    cursoId = models.ForeignKey(to=Curso, db_column='curso_id', on_delete=models.CASCADE)
    estudianteId = models.ForeignKey(to=Estudiante, db_column='estudiante_id', on_delete=models.CASCADE)

    class Meta:
        db_table = 'curso_estudiante'

class Calificacion(models.Model):
    id = models.AutoField(primary_key=True, unique=True, null=False)
    pc1 = models.FloatField(null=False)
    pc2 = models.FloatField(null=False)
    pc3 = models.FloatField(null=False)
    examenFinal = models.FloatField(db_column='examen_final' ,null=False)
    cursoId = models.ForeignKey(to=Curso, db_column='curso_id', on_delete=models.CASCADE, related_name='curso')

    class Meta:
        db_table = 'calificaciones'