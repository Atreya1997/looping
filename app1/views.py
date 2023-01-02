from django.shortcuts import render

# Create your views here.
def looping(request):
    d={'name' : 'Atreya'}
    return render(request,'looping.html',d)