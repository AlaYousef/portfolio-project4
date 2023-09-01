from . import views
from django.urls import path

urlpatterns = [
    path('', views.RecipeList.as_view(), name='home'),
    path('coctailes/', views.CoctailesList.as_view(), name='coctailes'),
    path('dinner/', views.DinnerList.as_view(), name='dinner'),
    path('sweets/', views.SweetsList.as_view(), name='sweets'),
    path('recipes/<int:id>/', views.RecipeDetail.as_view(),
         name='recipe_detail'),
    path('like/<int:id>', views.RecipeLike.as_view(), name='recipe_like'),
    path('bookmarked/<int:id>', views.RecipeBookmarked.as_view(),
         name='recipe_bookmarked'),
    path('bookmarks/', views.MyBookmarkRecipe.as_view(), name='mybookmarks'),
    path('addrecipe/', views.AddRecipe.as_view(), name='add_recipe'),
    path('myrecipes/', views.MyRecipes.as_view(), name='my_recipes'),
    path('recipe/<int:pk>', views.DeleteRecipe.as_view(),
         name='delete_recipe'),
    path('recipe/<int:pk>/edit', views.EditRecipe.as_view(),
         name='edit_recipe'),
    path('comment/<int:pk>/deletecomment', views.DeleteComment.as_view(),
         name='delete_comment'), ]
