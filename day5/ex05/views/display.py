from django import db
from django.views import View
from django.http import HttpResponse
from django.shortcuts import render
from ..models import Movies


class Display(View):
    template = 'ex05/display.html'
    def get(self, request):
        response = None
        try :
            response = Movies.objects.all()
        except Exception as e :
            return HttpResponse("No data available")
        if response :
            return render(request, self.template, {'data' : response})
        else :
            return HttpResponse("No data available")

