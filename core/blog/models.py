from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse


# User = get_user_model()
class Post(models.Model):
    # This is a class to define posts for blog app
    title = models.CharField(max_length=100)
    author = models.ForeignKey("accounts.Profile", on_delete=models.CASCADE)
    image = models.ImageField(blank=True, null=True)
    content = models.TextField()
    status = models.BooleanField(default=False)
    category = models.ForeignKey("Category", on_delete=models.SET_NULL, null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    published_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.title

    def get_snippet(self):
        return self.content[0:10]

    def get_absolute_url(self):
        return reverse("blog:api-v1:posts-detail", kwargs={"pk": self.pk})


class Category(models.Model):
    # This is a class to define categories for blog app
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
