from django.shortcuts import render
from .models import Telefon

# Create your views here.
def home(request):
    return render(request, 'home.html')

def telefon_list(request):
    telefons = Telefon.objects.all()
    context = {'telefons': telefons}
    return render(request, 'telefonlar/telefon_list.html',  context= context)

def  telefon_info(request,  pk):
    tele =Telefon.objects.get(id=pk)
    context = {'tele': tele}
    return render(request, 'telefonlar/telefon_info.html', context = context)