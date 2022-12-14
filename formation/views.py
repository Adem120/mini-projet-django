from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.template import loader
from formation.form import FormConnexion
from formation.models import Type, Diplome
from django.contrib.auth.decorators import login_required
@login_required(login_url='login/')
def index(request):
    D=Diplome.objects.all().values()
    T=Type.objects.all().values()
    template = loader.get_template('formation.html')
    context = {
    'D':D,
    'T':T
}
    return HttpResponse(template.render(context, request))
@login_required(login_url='login')
def type(request):
    T=Type.objects.all().values()
    template = loader.get_template('listetype.html')
    context = {
    'T':T
}
    return HttpResponse(template.render(context, request))
def signIn(request):
    connect_form = FormConnexion ()
    username = request.POST['login']
    password = request.POST['mot2pass']
    user = authenticate(request, username=username, password=password)
    
    if user is not None:
        login(request, user)
        request.session['username'] = username 
        return HttpResponseRedirect(reverse('formation'))

    else:
        print("Login et/ou mot de passe incorrect")
        #return HttpResponseRedirect(reverse('connect')) 
        return render(request,'login.html', {'connect_form' : connect_form,'error':True,})

def connect (request):
    connect_form = FormConnexion ()
    return render(request, 'login.html', {'connect_form' : connect_form ,'error':False})
@login_required(login_url='login')
def add(request):
    T=Type.objects.all().values()
    template = loader.get_template('ajoutdip.html')
    context = {
   'T':T
    }
    return HttpResponse(template.render(context,request))
@login_required(login_url='login')
def addtyp(request):
    template = loader.get_template('ajouttyp.html')
    context = {
   
    }
    return HttpResponse(template.render(context,request))
@login_required(login_url='login')
def modif(request,id):
    D=Diplome.objects.get(id=id)
    T=Type.objects.all().values()
    template = loader.get_template('modif.html')
    context = {
   'T':T,
   'D':D
    }

    return HttpResponse(template.render(context, request))
@login_required(login_url='login')
def modiftp(request,id):
    T=Type.objects.get(id=id)
    template = loader.get_template('modiftyp.html')
    context = {
   'T':T
    }

    return HttpResponse(template.render(context, request))
@login_required(login_url='login')
def del_dip(request, id):
    d = Diplome.objects.get(id=id)
    d.delete()
    return HttpResponseRedirect(reverse('formation'))
@login_required(login_url='login')
def del_typ(request, id):
    d = Type.objects.get(id=id)
    d.delete()
    return HttpResponseRedirect(reverse('type'))
@login_required(login_url='login')
def add_dip(request):
    diplom = request.POST['diplome']
    datefi= request.POST['datefin']
    c = request.POST['d']
    l = Type.objects.get(id=c)
    print(l)
    diplome = Diplome(diplome=diplom,datefin=datefi,Type=l)
    
    diplome.save()
    return HttpResponseRedirect(reverse('formation'))
@login_required(login_url='login')
def add_typ(request):
    typ = request.POST['type']
    desc= request.POST['desc']
    
    l=Type(TypeName=typ,description=desc)
    
    l.save()
    return HttpResponseRedirect(reverse('type'))
@login_required(login_url='login')
def modif_dip(request,id):
    diplom = request.POST['diplome']
    datefi= request.POST['datefin']
    c = request.POST['d']
    d=Diplome.objects.get(id=id)
    l = Type.objects.get(id=c)
    d.diplome=diplom
    d.datefin=datefi
    d.Type=l
    
    d.save()
    return HttpResponseRedirect(reverse('formation'))
@login_required(login_url='login')
def modif_typ(request,id):
    typ = request.POST['type']
    desc= request.POST['desc']
    l = Type.objects.get(id=id)
    l.TypeName=typ
    l.description=desc
    
    l.save()
    return HttpResponseRedirect(reverse('type'))
def signOut(request):
    logout(request) 
    return HttpResponseRedirect(reverse('portfolio'))
