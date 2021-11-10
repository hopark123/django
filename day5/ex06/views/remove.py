from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.views import View
from ..forms import RemoveForm
import psycopg2



class Remove(View):
    connection = psycopg2.connect(
        database=settings.DATABASES['default']['NAME'],
        user=settings.DATABASES['default']['USER'],
        password=settings.DATABASES['default']['PASSWORD'],
        host=settings.DATABASES['default']['HOST'],
    )
    template = "ex06/remove.html"

    def get(self, request):
        response = None
        res = ""
        curs = self.connection.cursor()
        try:
            curs.execute("""SELECT * FROM ex06_movies""")
            response = curs.fetchall()
            context = {'form' : RemoveForm(choices=((movie[0], movie[0]) for movie in response))}
        except Exception as e:
            res += str(e)
        finally:
            if curs and not curs.closed:
                curs.close()
        if response :
            return render(request, self.template, context)
        else:
            return HttpResponse(res, "No data available")
    
    def post(self, request) :
        res = ""
        curs = self.connection.cursor()
        try:
            curs.execute("""SELECT * FROM ex06_movies""")
            response = curs.fetchall()
            choices=((movie[0], movie[0]) for movie in response)
        except Exception as e:
            res += str(e)
        data = RemoveForm(choices, request.POST)
        DELETE_SQL = f"""
            DELETE FROM ex06_movies WHERE title = %s
            """
        if data.is_valid() == True:
            try:
                with self.connection.cursor() as curs:
                    curs.execute(DELETE_SQL, [data.cleaned_data['title']])
                self.connection.commit()
            except Exception as e:
                res += str(e)
            finally:
                self.connection.commit()
                if curs and not curs.closed:
                    curs.close()
        print(res)
        return redirect(request.path)

