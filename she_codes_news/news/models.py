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

    # Includes categories available to posting User
    categories = (
        ("MISC", "Misc"),
        ("TRAVELS", "Travels"),
        ("CODING", "Coding"),
        
    )

    category = models.CharField(max_length=200, choices=categories, default="Misc")