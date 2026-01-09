from django.urls import re_path, path
from . import views
from django.views.generic import TemplateView

app_name = 'ttest'

urlpatterns = [
    path('catdetail/<int:pk>/', views.CatDetailView.as_view(), name='cat-detail'),
    path('catlist/', views.CatListView.as_view(), name='cat-list'),
    path('game/<guess>', views.GameView.as_view(), name="game-view"),
    path('remain/<guess>', views.RestMainView.as_view()),
    path('main/', views.MainView.as_view()),
    path('', TemplateView.as_view(template_name='ttest/main.html')),
    path('danger', views.danger, name="danger-view"),
    path('rest/<guess>', views.rest),
    path("main/abc/", views.main),
    # re_path(r"^(?P<x>\w+)/", views.index),
    path("<int:any>", views.any_s)
]
