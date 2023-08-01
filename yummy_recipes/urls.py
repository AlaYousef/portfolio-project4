from . import views
from django.urls import path

urlpatterns = [
    path("", views.RecipeList.as_view(), name="home"),
    path("coctailes/", views.CoctailesList.as_view(), name="coctailes"),
]