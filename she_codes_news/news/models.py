from email.policy import default
from importlib.resources import contents
from unicodedata import category
from django.contrib.auth import get_user_model
from django.db import models


class NewsStory(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(
        get_user_model(),
        related_name='stories',
        on_delete=models.CASCADE
    )
    pub_date = models.DateTimeField()
    content = models.TextField()
    # Below is allowing the User to add images to posts
    image=models.URLField(null=True, blank=True)

    # Below is class to order stories by date (from newest to oldest)
    class Meta:
        ordering = ['-pub_date']

    categories = (
        ("TRAVELS", "Travels"),
        ("CODING", "Coding"),
        ("MISC", "Misc"),
    )

    category = models.CharField(max_length=200, choices=categories, default="Misc")
    


# Below: attempt to do something with images, I dont even know what is was all about:
# class Post(models.Model):
#     title=models.CharField(max_length=50)
#     image=models.URLField(null=True, blank=True)
