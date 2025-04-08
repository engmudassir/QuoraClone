from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('', views.home_view, name='home'),
    path('question/<int:question_id>/', views.question_detail_view, name='question_detail'),
    path('answer/<int:answer_id>/like/', views.like_answer_view, name='like_answer'),
    path('users/', views.user_list, name='user_list'),
]
