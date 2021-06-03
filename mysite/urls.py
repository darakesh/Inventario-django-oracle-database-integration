from django.urls import path
from . import views

urlpatterns = [
    path("",views.home_view , name = "home"),
    path("edit/<int:pk>/",views.edit_view, name = "edit" ),
    path("delete/<int:pk>/", views.delete_view, name = "delete"),
]