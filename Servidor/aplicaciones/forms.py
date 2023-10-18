from django import forms

class CrearPaciente(forms.ModelForm):
    rutPaciente = forms.CharField(max_length=12)
    nomPaciente = forms.CharField(max_length=50)
    apePaciente = forms.CharField(max_length=100)
    correo = forms.CharField(max_length=250)
    contraPaciente = forms.CharField(max_length=100)
    fechaNacimiento = forms.DateField()