from django import forms
from django.utils.text import slugify
from django.db import models
from django.contrib.auth.models import User
from djrichtextfield.models import RichTextField

# Create your models here.



class Note(models.Model):
    """Model for creating notes on a todo list"""
    user = models.ForeignKey(User, related_name="task_owner", on_delete=models.CASCADE, default=1)
    title = models.CharField(max_length=75, null=False, blank=False)
    note = RichTextField(max_length=500, null=False, blank=False)
    slug = models.SlugField(unique = True, blank = True)
    due_date = forms.DateField(
        widget=forms.DateInput(format='%d/%m/%Y', attrs={'placeholder': 'dd/mm/yyyy'}),
        input_formats=['%d/%m/%Y'],
        required=False
    )

    def __str__(self):
        return f"{self.title} | {self.due_date}"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)

        return super().save(*args, **kwargs)