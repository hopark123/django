from django.conf import settings
from django.http import HttpRequest
from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import HttpResponse
import time
import random

class SessionMiddleware(MiddlewareMixin):
    def process_request(self, request : HttpRequest) :
        if request.user.is_authenticated:
            return
        set_date = request.session.setdefault('set_date', time.time())  ## 값이 없으면 갑 새로 설정
        timeover = time.time() - set_date  > 42
        if timeover:
            request.session.flush()
        request.session.setdefault('anonymous', random.choice(settings.ANONMYMOUS_USERS))
        request.user.username = request.session.get('anonymous')