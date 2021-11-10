from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.views import View
from ..forms import UpdateForm
import psycopg2

class Update(View):
    connection = psycopg2.connect(
        database=settings.DATABASES['default']['NAME'],
        user=settings.DATABASES['default']['USER'],
        password=settings.DATABASES['default']['PASSWORD'],
        host=settings.DATABASES['default']['HOST'],
    )
    template = "ex06/update.html"
    def get(self, request):
        response = None
        res = ""
        curs = self.connection.cursor()
        try:
            curs.execute("""SELECT * FROM ex06_movies""")
            response = curs.fetchall()
            context = {'form' : UpdateForm(choices=((movie[0], movie[0]) for movie in response))}
        except Exception as e:
            res += str(e)
        finally:
            if curs and not curs.closed:
                curs.close()
        if response :
            return render(request, self.template, context)
        else:
            return HttpResponse(res, "No data available")
    
    def post(self, request):
        choices = {}
        SELECT_TABEL = f"""
            SELECT title FROM ex06_movies;
            """
        try:
            with self.conn.cursor() as curs:
                curs.execute(SELECT_TABEL)
                movies = curs.fetchall()
            choices = (
                (movie[0], movie[0]) for movie in movies)
        except Exception as e:
            print(e)
        data = UpdateForm(choices, request.POST)
        UPDATE_SQL = f"""
            UPDATE ex06_movies SET opening_crawl = %s WHERE title = %s
            """
        if data.is_valid() == True:
            try:
                with self.conn.cursor() as curs:
                    curs.execute(
                        UPDATE_SQL, [data.cleaned_data['opening_crawl'], data.cleaned_data['title']])
                self.conn.commit()
            except Exception as e:
                print(e)
        return redirect(request.path)