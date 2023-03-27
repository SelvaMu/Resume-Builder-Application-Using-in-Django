from django.contrib import admin
from django.urls import path
from . import views

urlpatterns=[
    path('',views.home,name="home"),
    path('generate',views.generate,name="generate"),
    # path('pdf1',views.pdf1,name='pdf'),
    # path("pdf2",views.pdf2,name="pdf2"),
]