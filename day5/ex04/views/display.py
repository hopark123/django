from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
import psycopg2


class Display(View):
    connection = psycopg2.connect(
        database=settings.DATABASES['default']['NAME'],
        user=settings.DATABASES['default']['USER'],
        password=settings.DATABASES['default']['PASSWORD'],
        host=settings.DATABASES['default']['HOST'],
    )
    def get(self, request):
        response = None
        res = ""
        try :
            curs = self.connection.cursor()
            try:
                curs.execute("""SELECT * FROM ex04_movies""")
                response = curs.fetchall()
            except Exception as e:
                res += str(e) + "<br>"
            finally:
                if curs and not curs.closed:
                    curs.close()
            if response:
                return render(request, 'ex04/display.html', {'data': response})
            else:
                return HttpResponse(res, "No data available")
        except Exception as e:
            return HttpResponse(res, "No data available")

