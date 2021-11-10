from django.conf import settings
from django.http import HttpRequest, HttpResponse
import psycopg2

def init(request:HttpRequest):
    try :
        connection = psycopg2.connect(
            database = settings.DATABASES['default']['NAME'],
            user = settings.DATABASES['default']['USER'],
            password = settings.DATABASES['default']['PASSWORD'],
            host = settings.DATABASES['default']['HOST'],
        )
        cursor = connection.cursor()
        cursor.execute("""
            CREATE TABLE ex00_movies(
                title VARCHAR(64) UNIQUE NOT NULL,
                episode_nb INT PRIMARY KEY,
                opening_crawl TEXT,
                director VARCHAR(32) NOT NULL,
                producer VARCHAR(128) NOT NULL,
                release_date DATE NOT NULL
                );
            """)
        connection.commit()
        res = "OK"
    except psycopg2.Error as e :
        res = str(e)
    if cursor and not cursor.closed :
        cursor.close()
    return HttpResponse(res)