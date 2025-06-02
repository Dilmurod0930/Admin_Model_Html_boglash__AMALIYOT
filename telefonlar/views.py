from django.shortcuts import render
from .models import Telefon

# Create your views here.
def home(request):
    return render(request, 'home.html')

def telefon_list(request):
    tele = Telefon.objects.all()
    context = {'tele': tele}
    return render(request, 'telefon/telefon_list.html',  context= context)

def  telefon_info(request,  id):
    tele = Telefon.objects.get(id=id)
    context = {'tele': tele}
    return render(request, 'telefon/telefon_info.html', context = context)