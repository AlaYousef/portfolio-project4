from . import views
from django.urls import path

urlpatterns = [
    path("", views.RecipeList.as_view(), name="home"),
    path("coctailes/", views.CoctailesList.as_view(), name="coctailes"),
    path("dinner/", views.DinnerList.as_view(), name="dinner"),
    path("sweets/", views.SweetsList.as_view(), name="sweets"),
    path('<slug:slug>/',  views.RecipeDetail.as_view(), name='recipe_detail'),
    path('like/<slug:slug>',  views.RecipeLike.as_view(), name='recipe_like'),
]