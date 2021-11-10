from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import FormView
from ..forms import CommentForm, ReplyForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from ..models import ArticleModel, CommentsModel, ReplyModel

class ArticleView(LoginRequiredMixin, FormView):
    form_comment = CommentForm
    form_reply = ReplyForm
    login_url = reverse_lazy('login')
    def get(self, request, article_id):
        article = get_object_or_404(ArticleModel, id=article_id)
        context = {
            'article' : article,
            'form_comment' : self.form_comment,
            'form_reply' : self.form_reply,
        }
        return render(request, 'view_article.html', context)

    def post(self, request, article_id):
        article = ArticleModel.objects.get(id=article_id)
        if request.POST.get('up_article') or request.POST.get('down_article'):
            article_obj = ArticleModel.objects.get(pk=request.POST.get('up_article') or request.POST.get('down_article'))
            if request.POST.get('up_article'):
                article_obj.upvote(request.user)
            else:
                article_obj.downvote(request.user)
        elif request.POST.get('delete_article') :
            article_obj = ArticleModel.objects.get(pk=request.POST.get('delete_article'))
            if not (article_obj.author != request.user and request.user.is_staff == False and request.user.is_superuser == False):
                ArticleModel.objects.get(pk=request.POST.get('delete_article')).delete()
                return redirect('/')
        elif request.POST.get('up_comment') or request.POST.get('down_comment'):
            comment_obj = CommentsModel.objects.get(pk=request.POST.get('up_comment') or request.POST.get('down_comment'))
            if request.POST.get('up_comment'):
                comment_obj.upvote(request.user)
            else:
                comment_obj.downvote(request.user)
        elif request.POST.get('up_reply') or request.POST.get('down_reply'):
            reply_obj = ReplyModel.objects.get(pk=request.POST.get('up_reply') or request.POST.get('down_reply'))
            if request.POST.get('up_reply'):
                reply_obj.upvote(request.user)
            else:
                reply_obj.downvote(request.user)
        context = {
            'article' : article,
            'form_comment' : self.form_comment,
            'form_reply' : self.form_reply,
        }
        return render(request, 'view_article.html', context)


class WriteCommentView(FormView):
    def post(self, request, article_id):
        if request.user.is_anonymous:
            return redirect('login')
        form = CommentForm(request.POST)
        if form.is_valid():
            temp_form = form.save(commit=False)
            temp_form.article = ArticleModel.objects.get(id=article_id)
            temp_form.author = self.request.user
            temp_form.save()

        return redirect('article', article_id)


class DeleteCommentView(FormView):
    def get(self, request, comment_id, article_id):
        comment = CommentsModel.objects.get(id=comment_id)
        if not (comment.author != request.user and request.user.is_staff == False and request.user.is_superuser == False):
            comment.delete()
        return redirect('article', article_id)


class WriteReplyView(FormView):
    def post(self, request, comment_id, article_id):
        if request.user.is_anonymous:
            return redirect('login')
        form = ReplyForm(request.POST)
        if form.is_valid():
            temp_form = form.save(commit=False)
            temp_form.comment = CommentsModel.objects.get(id=comment_id)
            temp_form.author = self.request.user
            temp_form.save()
        return redirect('article', article_id)


class DeleteReplyView(FormView):
    def get(self, request, reply_id, article_id):
        reply = ReplyModel.objects.get(id=reply_id)
        if not (reply.author != request.user and request.user.is_staff == False and request.user.is_superuser == False):
            reply.delete()
        return redirect('article', article_id)
