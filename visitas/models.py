from django.db import models

# Create your models here.

from django.db import models

class Visita(models.Model):
    fecha = models.DateField()
    supervisor = models.CharField(max_length=120)
    zona = models.CharField(max_length=120)
    observaciones = models.TextField(blank=True)
    estado = models.CharField(max_length=20, choices=[('completa','Completa'),('pendiente','Pendiente')])

    def __str__(self):
        return f"{self.fecha} - {self.supervisor} - {self.zona}"

class Checklist(models.Model):
    visita = models.ForeignKey(Visita, related_name='checklists', on_delete=models.CASCADE)
    item = models.CharField(max_length=200)
    cumplido = models.BooleanField(default=False)
    comentario = models.TextField(blank=True)
    nivel_riesgo = models.CharField(max_length=30, choices=[('bajo','Bajo'),('medio','Medio'),('alto','Alto')])

    def __str__(self):
        return f"{self.item} - {self.nivel_riesgo}"
