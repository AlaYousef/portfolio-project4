from django.shortcuts import render, get_object_or_404, reverse
from django.contrib.messages.views import SuccessMessageMixin
from django.views import generic, View
from django.http import HttpResponseRedirect
from .models import Recipe
from .forms import CommentForm


class RecipeList(generic.ListView):
    model = Recipe
    queryset = Recipe.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'
    paginate_by = 6


class DinnerList(generic.ListView):
    model = Recipe
    queryset = Recipe.objects.filter(status=1, category=0).order_by('-created_on')
    template_name = 'dinner.html'
    paginate_by = 6


class CoctailesList(generic.ListView):
    model = Recipe
    queryset = Recipe.objects.filter(status=1, category=2).order_by('-created_on')
    template_name = 'coctailes.html'
    paginate_by = 6


class SweetsList(generic.ListView):
    model = Recipe
    queryset = Recipe.objects.filter(status=1, category=1).order_by('-created_on')
    template_name = 'sweets.html'
    paginate_by = 6


class RecipeDetail(View):
    
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
                "comment_form": CommentForm
            },
        )


class RecipeLike(View):
    
    def post(self, request, slug, *args, **kwargs):
        recipe = get_object_or_404(Recipe, slug=slug)
        if recipe.likes.filter(id=request.user.id).exists():
            recipe.likes.remove(request.user)
        else:
            recipe.likes.add(request.user)

        return HttpResponseRedirect(reverse('recipe_detail', args=[slug]))


class RecipeBookmarked(View):
    
    def post(self, request, slug, *args, **kwargs):
        recipe = get_object_or_404(Recipe, slug=slug)
        if recipe.bookmarked.filter(id=request.user.id).exists():
            recipe.bookmarked.remove(request.user)
        else:
            recipe.bookmarked.add(request.user)

        return HttpResponseRedirect(reverse('recipe_detail', args=[slug]))
