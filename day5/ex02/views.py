from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from django.conf import settings
import psycopg2


def init(request: HttpRequest):
    try:
        connection = psycopg2.connect(
            database=settings.DATABASES['default']['NAME'],
            user=settings.DATABASES['default']['USER'],
            password=settings.DATABASES['default']['PASSWORD'],
            host=settings.DATABASES['default']['HOST'],
        )
        cursor = connection.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS ex02_movies(
                title VARCHAR(64) UNIQUE NOT NULL,
                episode_nb INT PRIMARY KEY,
                opening_crawl TEXT,
                director VARCHAR(32) NOT NULL,
                producer VARCHAR(128) NOT NULL,
                release_date DATE NOT NULL
                );
            """)
        connection.commit()
        ret = "OK"
        return HttpResponse(ret)
    except psycopg2.Error as e:
        ret = str(e)
    finally:
        connection.close()
    return HttpResponse(ret)


def populate(request: HttpResponse):
    res = ""
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
    try:
        connection = psycopg2.connect(
            database=settings.DATABASES['default']['NAME'],
            user=settings.DATABASES['default']['USER'],
            password=settings.DATABASES['default']['PASSWORD'],
            host=settings.DATABASES['default']['HOST'],
        )
        curs = connection.cursor()
        for movie in data:
            try:
                insert_stmt = """INSERT INTO 
                ex02_movies (
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
                connection.commit()
                res += "OK<br>"
            except Exception as e:
                connection.rollback()
                res += "[" + str(e) + "]" + "<br>"
    except Exception as e:
        res += "{" + str(e) + "}"
    finally:
        if curs and not curs.closed:
            curs.close()
        return HttpResponse(res)


def display(request: HttpResponse):
    response = None
    res = ""
    try :
        connection = psycopg2.connect(
            database=settings.DATABASES['default']['NAME'],
            user=settings.DATABASES['default']['USER'],
            password=settings.DATABASES['default']['PASSWORD'],
            host=settings.DATABASES['default']['HOST'],
        )
        curs = connection.cursor()
        try:
            curs.execute("""SELECT * FROM ex02_movies""")
            response = curs.fetchall()
        except Exception as e:
            res += str(e) + "<br>"
        finally:
            if curs and not curs.closed:
                curs.close()
        if response:
            return render(request, 'ex02/display.html', {'data': response})
        else:
            return HttpResponse(res, "No data available")
    except Exception as e:
        return HttpResponse(res, "No data available")