from . import views
from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.MainView.as_view(), name="main"),
    path('register', views.RegisterView.as_view(), name="register"),
    path('logout/', views.LogOutView.as_view(), name="logout"),
    path('login/', views.LoginView.as_view(), name="login"),
    path('post/', views.AddArticle.as_view(), name="add_article"),
    path('detail/<int:article_id>', views.ArticleView.as_view(),  name="article"),
    path('profile/<int:userid>', views.ProfileView.as_view(),  name="profile"),
    path('profile/modify', views.ProfileModifyView.as_view(),  name="modify_profile"),
    path('write_comment/<int:article_id>', views.WriteCommentView.as_view(), name="write_comment"),
    path('delete_comment/<int:comment_id>/<int:article_id>', views.DeleteCommentView.as_view(), name="delete_comment"),
    path('write_reply/<int:comment_id>/<int:article_id>', views.WriteReplyView.as_view(), name="write_reply"),
    path('delete_reply/<int:reply_id>/<int:article_id>', views.DeleteReplyView.as_view(), name="delete_reply"),
]
