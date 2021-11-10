from django.views.generic import FormView
from ..forms import ArticleForm
from ..models import ArticleModel
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect


class AddArticle(LoginRequiredMixin, FormView):
    template_name = "add_article.html"
    form_class = ArticleForm
    success_url = reverse_lazy('main')
    login_url = reverse_lazy('login')

    def get(self, request):
       form = self.form_class(initial=self.initial)
       return render(request, self.template_name, {'form': form,})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            content = form.cleaned_data['content']
            ArticleModel.objects.create(
                title=title,
                content=content,
                author=self.request.user,
            )
        return redirect('main')
