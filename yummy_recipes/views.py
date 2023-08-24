from django.shortcuts import render, get_object_or_404, reverse
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views import generic, View
from django.http import HttpResponseRedirect
from .models import Recipe, Comment
from .forms import CommentForm, RecipeForm
from django.db.models.signals import pre_save
from django.urls import reverse_lazy


class RecipeList(generic.ListView):
    """
    This view display a list of recipes.
    """
    model = Recipe
    queryset = Recipe.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'
    paginate_by = 6


class DinnerList(generic.ListView):
    """
    This view display a list of recipes if category value is 0, which is for dinner recipes
    """
    model = Recipe
    queryset = Recipe.objects.filter(status=1, category=0).order_by('-created_on')
    template_name = 'dinner.html'
    paginate_by = 6


class CoctailesList(generic.ListView):
    """
    This view display a list of recipes if category value is 2, which is for dinner recipes
    """
    model = Recipe
    queryset = Recipe.objects.filter(status=1, category=2).order_by('-created_on')
    template_name = 'coctailes.html'
    paginate_by = 6


class SweetsList(generic.ListView):
    """
    This view display a list of recipes if category value is 1, which is for dinner recipes
    """
    model = Recipe
    queryset = Recipe.objects.filter(status=1, category=1).order_by('-created_on')
    template_name = 'sweets.html'
    paginate_by = 6


class RecipeDetail(View):
    """
    This class based view display the all detailes of a selected recipe.
    """
    def get(self, request, slug, *args, **kwargs):
        queryset = Recipe.objects.filter(status=1)
        recipe = get_object_or_404(queryset, slug=slug)
        comments = recipe.comments.filter(approved=True).order_by('created_on')
        liked = False
        bookmark = False
        if recipe.likes.filter(id=self.request.user.id).exists():
            liked = True
        
        if recipe.bookmarked.filter(id=self.request.user.id).exists():
            bookmark = True

        jls_extract_var = "recipe_detail.html"
        return render(
            request,
            jls_extract_var,
            {
                "recipe": recipe,
                "comments": comments,
                "commented": False,
                "liked": liked,
                "bookmark": bookmark,
                "comment_form": CommentForm()
            },
        )

    def post(self, request, slug, *args, **kwargs):
        """
        This method is called if the user make a POST request
        via the like, bookmarke or comment forms.
        """
        queryset = Recipe.objects.filter(status=1)
        recipe = get_object_or_404(queryset, slug=slug)
        comments = recipe.comments.filter(approved=True).order_by('created_on')
        liked = False
        bookmark = False
        success_message = "%(name)s was created successfully"

        if recipe.likes.filter(id=self.request.user.id).exists():
            liked = True
        
        if recipe.bookmarked.filter(id=self.request.user.id).exists():
            bookmark = True

        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment_form.instance.email = request.user.email
            comment_form.instance.name = request.user.username
            comment = comment_form.save(commit=False)
            comment.recipe = recipe
            comment.save()
        else:
            comment_form = CommentForm() 

        jls_extract = "recipe_detail.html"
        return render(
            request,
            jls_extract,
            {
                "recipe": recipe,
                "comments": comments,
                "commented": True,
                "liked": liked,
                "bookmark": bookmark,
                "comment_form": CommentForm()
            },
        )


class RecipeLike(View):
    """
    This view allows a logged in user to like/dislike recipes
    by checks if user id already exists in the like
    field in the Recipe model. If is it, when the user click on like btn 
    the user id will be removed.
    """
    def post(self, request, slug, *args, **kwargs):
        recipe = get_object_or_404(Recipe, slug=slug)
        if recipe.likes.filter(id=request.user.id).exists():
            recipe.likes.remove(request.user)
            
        else:
            recipe.likes.add(request.user)
        
        return HttpResponseRedirect(reverse('recipe_detail', args=[slug]))


class RecipeBookmarked(View):
    """
    This view allows a logged in user to bookmark recipes
    by checks if user id already exists in the bookmarked
    field in the Recipe model. If is it, when the user click on it 
    the user id will be removed.
    """
    
    def post(self, request, slug, *args, **kwargs):
        recipe = get_object_or_404(Recipe, slug=slug)
        if recipe.bookmarked.filter(id=request.user.id).exists():
            recipe.bookmarked.remove(request.user)
            messages.success(self.request, 'Recipe removed from bookmarks page')
        else:
            recipe.bookmarked.add(request.user)
            messages.success(self.request, 'Recipe added to bookmarks page')

        return HttpResponseRedirect(reverse('recipe_detail', args=[slug]))


class MyBookmarkRecipe(generic.ListView):
    """
    This view allows a logged in user to display all their bookmarked 
    recipes on mybookmarks.html page.
    """
    model = Recipe
    template_name = 'mybookmarks.html'
    paginate_by = 6

    def get_queryset(self):
        """Override get_queryset to filter by user favourites"""
        return Recipe.objects.filter(bookmarked=self.request.user.id)


class AddRecipe(SuccessMessageMixin, generic.CreateView):
    
    form_class = RecipeForm
    template_name = 'add_recipe.html'
    success_message = "recipe was created successfully"

    def form_valid(self, form):
        """
        called when the form is valid,
        and set the user as author of the recipe
        """
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    def get_success_message(self, request):
        return self.success_message


class MyRecipes(generic.ListView):
    model = Recipe
    template_name = 'my_recipes.html'
    paginate_by = 6

    def get_queryset(self):
        return Recipe.objects.filter(author=self.request.user)


class DeleteRecipe(generic.DeleteView):
    """
    Allow logged in users to delete recipes that they created
    """
    model = Recipe
    template_name = 'delete_recipe.html'
    success_message = "Recipe deleted successfully"
    """
    URL TO REDIRECT-TO AFTER DELETING
    From: https://stackoverflow.com/questions/31275574/
    reverse-for-success-url-on-django-class-based-view-complain-about-circular-impor
    """
    success_url = reverse_lazy('my_recipes')

    def test_func(self):
        recipe = self.get_object()
        return self.request.user == recipe.author

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(DeleteRecipe, self).delete(request, *args, **kwargs)


class EditRecipe(SuccessMessageMixin, generic.UpdateView):

    """
    This view  allow logged in users to edit their own recipes
    """
    model = Recipe
    form_class = RecipeForm
    template_name = 'edit_recipe.html'
    success_message = "Recipe was edited successfully"

    def form_valid(self, form):
        """
        called when the form is valid
        logged in user are the author of the recipe
        """
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        """
        allow only the recipe owner to edit it
        """
        recipe = self.get_object()
        return recipe.author == self.request.user

    def get_success_message(self, cleaned_data):
        return self.success_message 


class DeleteComment(generic.DeleteView):
    model = Comment
    form_class = CommentForm
    template_name = 'delete_comment.html'
    success_message = "Your comment deleted successfully"
    
    def test_func(self):
        """
        allow only the comment writer to delete it
        """
        comment = self.get_object()
        return comment.name == self.request.user.username

    def delete(self, request, *args, **kwargs):
        """
        Display sucess message given
        From: https://stackoverflow.com/questions/24822509/
        success-message-in-deleteview-not-shown
        """
        messages.success(self.request, self.success_message)
        return super(DeleteComment, self).delete(request, *args, **kwargs)
    
    def get_success_url(self):
        """ Return to recipe detail after deleting comment"""
        recipe = self.object.recipe
        return reverse_lazy('recipe_detail', kwargs={'slug': recipe.slug})
   

  