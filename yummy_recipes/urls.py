from . import views
from django.urls import path

urlpatterns = [
    path("", views.RecipeListList.as_view(), name="home"),
]