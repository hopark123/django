from django import db
from django.views import View
from django.http import HttpResponse
from django.shortcuts import redirect, render
from ..models import Movies
from ..forms import RemoveForm

class Remove(View):
    template = "ex05/remove.html"
    def get(self, request) :
        try :
            response = Movies.objects.all()
        except Exception as e :
            return HttpResponse(e, "No data available")
        if response :
            choices=((movie.title, movie.title) for movie in response)
            context = {"data" : RemoveForm(choices)}
            return render(request, self.template, context)
        else :
            return HttpResponse("No data available")
    
    def post(self, request) :
        response = None
        res = ""
        try :
            response = Movies.objects.all()
        except Exception as e :
            res += str(e)
            return redirect(request.path)
        if response :
            choices=((movie.title, movie.title) for movie in response)
            data = RemoveForm(choices, request.POST)
        if data.is_valid() == True:
            try:
                Movies.objects.get(title=data.cleaned_data['title']).delete()
            except Exception as e:
                res += str(e) + "\n"
        print(res)
        return redirect(request.path)