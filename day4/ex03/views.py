from django.shortcuts import render

# Create your views here.

def color(request):
    return render(request, 'ex03/index.html', {'rows': range(255, 0, -5)})