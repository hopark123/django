from django.conf import settings
from django.db import models


class ArticleModel(models.Model):
    title = models.CharField(max_length=128)
    content = models.TextField(null=False)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE)
    # 1 user : N articles
    date = models.DateTimeField(auto_now_add=True)
    upvotes = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='upvotes_article')
    downvotes = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='downvotes_article')

    def upvote(self, user):
        if self.downvotes.filter(id=user.id).count():
            self.downvotes.remove(user)
        if self.upvotes.filter(id=user.id).count():
            self.upvotes.remove(user)
        else:
            self.upvotes.add(user)

    def downvote(self, user):
        if self.upvotes.filter(id=user.id).count():
            self.upvotes.remove(user)
        if self.downvotes.filter(id=user.id).count():
            self.downvotes.remove(user)
        else:
            self.downvotes.add(user)
    
    def __str__(self):
        return self.title
