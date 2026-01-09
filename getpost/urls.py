from django.urls import path
from . import views


urlpatterns=[
    path('failform/', views.failform, name='failform'),
    path('csrfform/', views.csrfform, name="csrffrom"),
    path('guess/', views.guess, name='guess'),
]