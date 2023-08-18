from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.urls import reverse

STATUS = ((0, "Draft"), (1, "Published"))
CATEGORY = ((0, "Dinner"), (1, "Sweets"), (2, "Coctailes"))


class Recipe(models.Model):
    category = models.IntegerField(choices=CATEGORY, default=0)
    name = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True, null=False)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="recipe_posts"
    )
    featured_image = CloudinaryField('image', default='placeholder')
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    description = models.TextField()
    ingredients = models.TextField()
    steps = models.TextField()
    cook_time = models.CharField(max_length=100)
    status = models.IntegerField(choices=STATUS, default=0)
    likes = models.ManyToManyField(
        User, related_name='recipe_like', blank=True)
    bookmarked = models.ManyToManyField(
        User, related_name='recipe_bookmarked', blank=True)
    
    class Meta:
        ordering = ["-created_on"]

    def get_absolute_url(self):
        """Get url after user adds/edits recipe"""
        return reverse('recipe_detail', kwargs={'slug': self.slug})

    def __str__(self):
        return f"{self.name}"

    def number_of_likes(self):
        return self.likes.count()




class Comment(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE,
                               related_name="comments")
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ["created_on"]


    def __str__(self):
        return f"Comment {self.body} by {self.name}"


