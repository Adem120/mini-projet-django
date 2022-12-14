from django.http import HttpResponse
from django.shortcuts import render

from formation.models import Diplome, Experience, Skills, Type
from django.template import loader
# Create your views here.

def portfolio(request):
    D=Diplome.objects.all().values()
    T=Type.objects.all().values()
    S=Skills.objects.all().values()
    E=Experience.objects.all().values()
    template = loader.get_template('portfolio.html')
    context = {
    'D':D,
    'T':T,
    'S':S,
    'E':E   
}
    return HttpResponse(template.render(context, request))
def config(request):
    return render(request,'config.html')
