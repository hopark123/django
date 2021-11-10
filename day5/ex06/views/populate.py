from django.conf import settings
from django.http.response import HttpResponse
from django.views import View
import psycopg2

data = [
        {
            'title': "The Phantom Menace",
            'episode_nb': 1,
            'opening_crawl': "",
            'director': "George Lucas",
            'producer': "Rick McCallum",
            'release_date': "1999-05-19"
        },
        {
            'title': "Attack of the Clones",
            'episode_nb': 2,
            'opening_crawl': "",
            'director': "George Lucas",
            'producer': "Rick McCallum",
            'release_date': "2005-05-16"
        },
        {
            'title': "Revenge of the Sith",
            'episode_nb': 3,
            'opening_crawl': "",
            'director': "George Lucas",
            'producer': "Rick McCallum",
            'release_date': "2005-05-19"
        },
        {
            'title': "A New Hope",
            'episode_nb': 4,
            'opening_crawl': "",
            'director': "George Lucas",
            'producer': "Gary Kurtz, Rick McCallum",
            'release_date': "1999-05-19"
        },
        {
            'title': "The Empire Strikes Back",
            'episode_nb': 5,
            'opening_crawl': "",
            'director': "Irvin Kershner",
            'producer': "Gary Kutz, Rick McCallum",
            'release_date': "1980-05-17"
        },
        {
            'title': "Return of the Jedi",
            'episode_nb': 6,
            'opening_crawl': "",
            'director': "George Lucas",
            'producer': "Howard G. Kazanjian, George Lucas, Rick McCallum",
            'release_date': "1983-05-25"
        },
        {
            'title': "The Force Awakens",
            'episode_nb': 7,
            'opening_crawl': "",
            'director': "J. J. Abrams",
            'producer': "Kathleen Kennedy, J. J. Abrams, Bryan Burk",
            'release_date': "2015-12-11"
        },
    ]
class Populate(View):
    connection = psycopg2.connect(
    database=settings.DATABASES['default']['NAME'],
    user=settings.DATABASES['default']['USER'],
    password=settings.DATABASES['default']['PASSWORD'],
    host=settings.DATABASES['default']['HOST'],
    )
    def get(self, request) :
        res = ""
        curs = self.connection.cursor()
        for movie in data:
            try:
                insert_stmt = """INSERT INTO 
                ex06_movies (
                    title, 
                    episode_nb, 
                    opening_crawl, 
                    director, 
                    producer, 
                    release_date
                    )
                VALUES (%s, %s, %s, %s, %s, %s) 
                """
                curs.execute(insert_stmt, [movie['title'], movie['episode_nb'], movie['opening_crawl'],
                             movie['director'], movie['producer'], movie['release_date']])
                self.connection.commit()
                res += "OK<br>"
            except Exception as e:
                self.connection.rollback()
                res += "[" + str(e) + "]" + "<br>"
        if curs and not curs.closed:
            curs.close()
        return HttpResponse(res)