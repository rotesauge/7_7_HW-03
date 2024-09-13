from django.urls import path
# Импортируем созданное нами представление
from .views import (PostList,
                    PostDetail,
                    craate_post,
                    ArticleList,
                    ArticleDetail,
                    PostUpdate,
                    PostCreate,
                    PostDelete,
                    ArticleCreate,
                    ArticleUpdate,
                    ArticleDelete)


urlpatterns = [
   path('articles/', ArticleList.as_view(),name='articles'),
   path('articles/<int:pk>', ArticleDetail.as_view(), name='article'),
   path('articles/create/', ArticleCreate.as_view(), name='article_create'),
   path('articles/<int:pk>/update/', ArticleUpdate.as_view(), name='article_update'),
   path('articles/<int:pk>/delete/', ArticleDelete.as_view(), name='article_delete'),

   path('news/', PostList.as_view(),name='news'),
   path('news/<int:pk>', PostDetail.as_view(),name='post'),
   #path('news/create/', craate_post,name='post_create'),
   path('news/create/', PostCreate.as_view(),name='post_create'),
   path('news/<int:pk>/update/', PostUpdate.as_view(), name='post_update'),
   path('news/<int:pk>/delete/', PostDelete.as_view(), name='post_delete'),
]