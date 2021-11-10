from django.conf.urls import url
from ex02 import views

urlpatterns = [
    url(r'^$', views.main, name='ex02'),
    url(r'^post', views.post, name='post'),
]
