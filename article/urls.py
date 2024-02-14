from django.contrib import admin
from django.urls import path
from . import views
app_name="article1"
urlpatterns = [
   path("create/",views.about),
   path('update/<int:id>', views.update,name="update"),
   path('articles/', views.articles,name="articles"),
   path('delete/<int:id>', views.delete,name="delete"),
   path('details/<int:id>', views.details,name="details"),
]    

