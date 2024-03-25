from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views


urlpatterns = [
    path('', views.welcome, name='welcome'),
    path('index/', views.index, name='index'),
    path('allblog/', views.allblog, name='allblog'),
    path('allblogcard/', views.allblogcard, name='allblogcard'),
    path('blog/<int:post_id>/', views.blog_detail, name='blog_detail'),
    path('signup/', views.signup, name='signup'),
    path('login_index/', views.login_index, name='login_index'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),


    #  path fr filter category based posts
    path('category/<int:cat_id>/', views.category_based_posts, name='category'),

]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)