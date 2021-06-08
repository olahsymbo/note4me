from django.db import models
from django.utils import timezone


class Category(models.Model):

    name = models.CharField(max_length=300)

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name


class Notes(models.Model):

    title = models.CharField(max_length=300)
    content = models.TextField(blank=True)
    created = models.DateField(default=timezone.now().strftime("%Y-%m-%d"))
    due_date = models.DateField(default=timezone.now().strftime("%Y-%m-%d"))
    category = models.ForeignKey(Category, default="general", on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Notes"
        verbose_name_plural = "Notes"
        ordering = ["-created"]

    def __str__(self):
        return self.title
