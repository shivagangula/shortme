from django.db import models
# from django.contrib.auth.models import User
from django.urls import reverse


class UrlDetailes(models.Model):
    """
        # user field for authanticate
   user = models.OneToOneField(User)
        # click_n_time means number of times link clicked
   click_n_time = models.IntegerField()
        # is_active means url availble nor not for redirect
   is_active = models.BooleanField()
    """
    original_url = models.CharField(max_length=1000)
    shorted_url = models.SlugField()
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created"]

    def __str__(self):
        return f"Short Url for: {self.original_url} is {self.shorted_url}"

    def get_absolute_url(self):
        return reverse('slug', args=[str(self.slug)])
