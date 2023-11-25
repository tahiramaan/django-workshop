from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home_index'),
    path('results/<str:usn>',views.results),
    path('marks/<int:marks>',views.marks),
    path('login',views.login),

    path('posts/',views.PostList.as_view(),name="post"),
    path('post/<slug:slug>/',views.PostDetail.as_view(),name='postdetails')
]