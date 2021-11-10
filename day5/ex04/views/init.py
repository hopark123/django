from django.conf import settings
from django.views import View
from django.http import HttpRequest, HttpResponse
import psycopg2

class Init(View):
    connection = psycopg2.connect(
        database=settings.DATABASES['default']['NAME'],
        user=settings.DATABASES['default']['USER'],
        password=settings.DATABASES['default']['PASSWORD'],
        host=settings.DATABASES['default']['HOST'],
    )
    def get(self, request) :
        try :
            cursor = self.connection.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS ex04_movies(
                    title VARCHAR(64) UNIQUE NOT NULL,
                    episode_nb INT PRIMARY KEY,
                    opening_crawl TEXT,
                    director VARCHAR(32) NOT NULL,
                    producer VARCHAR(128) NOT NULL,
                    release_date DATE NOT NULL
                    )
                """)
            ret = "OK"
            self.connection.commit()
            return HttpResponse(ret)
        except Exception.Error as e:
            ret = str(e)
        finally:
            if cursor and not cursor.closed:
                cursor.close()
        return HttpResponse(ret)