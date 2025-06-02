from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html')

def telefon_list(request):
    return render(request, 'telefonlar/telefon_list.html')

def  telefon_info(request):
    return render(request, 'telefonlar/telefon_info.html')