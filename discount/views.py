from django.shortcuts import render
from .models import Sample
# Create your views here.
def sample(request):
    data = Sample.objects.all()
    
    return render(request, 'home.html', {'data':data})