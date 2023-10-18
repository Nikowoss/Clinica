from django.db import models

class Paciente(models.Model):
    rutPaciente = models.CharField(max_length=20)
    nomPaciente = models.CharField(max_length=100)
    apePaciente = models.CharField(max_length=100)
    correo = models.EmailField()
    contraPaciente = models.CharField(max_length=100)
    fechaNacimiento = models.DateField()
