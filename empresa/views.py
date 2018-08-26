from django.shortcuts import render
from administracion.models import Alumno, Habilidades, Estudio
from django.http import HttpResponse
from django.template import loader
from datetime import date
# Create your views here.
def index(request):
	ultimos_alumnos = Alumno.objects.all()
	template = loader.get_template('empresa/index.html')
	context = {
		'ultimos_alumnos': ultimos_alumnos,
	}
	return HttpResponse(template.render(context, request ))

def calcular_edad(nacimiento):
	hoy = date.today()
	return hoy.year - nacimiento.year - ((hoy.month, hoy.day) < (nacimiento.month,nacimiento.day))

def detalle(request, alumno_id):
	try:
		alumno = Alumno.objects.get(pk=alumno_id)
		habilidades = Habilidades.objects.filter(alumno=alumno)
		estudios = Estudio.objects.filter(alumno=alumno)
		edad = calcular_edad(alumno.fecha_nacimiento)
		context	= {
			'alumno': alumno,
			'lista_habilidades': habilidades,
			'estudios': estudios,
			'edad': edad,
		}
	except Alumno.DoesNotExist:
		raise Http404("Alumno no existe")
	return render(request,'empresa/detalle.html',context)