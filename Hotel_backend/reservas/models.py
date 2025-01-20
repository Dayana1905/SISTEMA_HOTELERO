from django.db import models

# Create your models here.
class Cliente(models.Model):
    cedula = models.CharField(max_length=10,primary_key=True, blank=False)
    nombre = models.CharField(max_length=50, blank=False)
    apellido = models.CharField(max_length=50, blank=False)
    correo = models.EmailField(blank=False)
    telefono = models.CharField(max_length=10)
    direccion = models.CharField(max_length=100)
    def _str_(self):
        return f'{self.cedula} - {self.nombre} - {self.apellido}' #self.nombre

class Habitacion(models.Model):
    codigo = models.CharField( max_length=10, primary_key=True)
    numero = models.CharField(max_length=10)
    tipo = models.CharField(max_length=50)
    precio = models.DecimalField(max_digits=10, decimal_places=2)

    def _str_(self):
        return f'Habitación {self.numero} - {self.tipo}'

class Reserva(models.Model):
    cedula = models.ForeignKey(Cliente, on_delete=models.RESTRICT)
    codigo = models.ForeignKey(Habitacion, on_delete=models.CASCADE)
    fecha_ingreso = models.DateField()
    fecha_salida = models.DateField()
    def _str_(self):
        return f'Reserva de {self.cliente.nombre} en habitación {self.habitacion.numero}'