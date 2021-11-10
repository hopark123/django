from django.shortcuts import render
from django.core.paginator import Paginator
from django.views.generic import View
from ..models import ArticleModel

class MainView(View):
    template_name = 'main.html'
    def get(self, request) :
        page = request.GET.get('page', '1')
        try:
            article = ArticleModel.objects.all().order_by('-date')
        except Exception as e:
            article = []
        paginator = Paginator(article, 10)
        page_obj = paginator.get_page(page)
        context = {
            'articles': page_obj,
        }
        return render(request, self.template_name, context)
    def  post(self, request):
        return render(request, self.template_name)



