from django.urls import path

from . import views

# app_name = "encyclopedia"
urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:title>", views.view, name="view"),
    path("search/", views.search, name="search"),
    path("create/", views.create, name="create"),
    path("edit/", views.edit, name="edit"),
    path("save_edit/", views.save_edit, name="save_edit"),
    path("random/", views.random, name="random"),
    
   
   
    
]
