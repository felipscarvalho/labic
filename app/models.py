from django.db import models
from markdownx.models import MarkdownxField
from markdownx.utils import markdownify
from django.contrib.auth.models import AbstractUser

# Create your models here.


class PostOptions(models.IntegerChoices):
    private = 0, 'Private'
    public = 1, 'Public'


class UserOptions(models.IntegerChoices):
    unknown = 0, 'Unknown'
    voluntario = 1, 'Voluntário'
    bolsista = 2, 'Bolsista'
    orientador = 3, 'Orientador'
    admin = 4, 'Administrador'


class ExtendUser(AbstractUser):
    profile_photo = models.ImageField(
        upload_to='profile/', default='defaults/profile_default.png')
    description = models.CharField(max_length=224, blank=True)
    user_level = models.IntegerField(
        choices=UserOptions.choices, default=UserOptions.unknown)

    def __str__(self):
        if (self.first_name):
            return f"{self.first_name} {self.last_name}"
        else:
            return self.username


class Projects(models.Model):
    cover = models.ImageField(upload_to='projects/',
                              default='defaults/projects_default.png')
    title = models.CharField(max_length=255, default='Untitled')
    description = models.TextField(default='')
    author = models.ForeignKey(
        ExtendUser, on_delete=models.CASCADE, blank=True, null=True, default=None)
    markdownFile = MarkdownxField()
    project_status = models.IntegerField(
        choices=PostOptions.choices, default=PostOptions.private)
    created_date = models.DateField(auto_now_add=True)

    @property
    def formatted_markdown(self):
        return markdownify(self.markdownFile)

    def get_absolute_url(self):
        return reverse('markdown-detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.title


class Articles(models.Model):
    cover = models.ImageField(upload_to='articles/',
                              default='defaults/articles_default.png')
    title = models.CharField(max_length=255, default='Untitled')
    description = models.TextField(default='')
    author = models.ForeignKey(
        ExtendUser, on_delete=models.CASCADE)
    markdownFile = MarkdownxField()
    post_status = models.IntegerField(
        choices=PostOptions.choices, default=PostOptions.private)
    project = models.ForeignKey(
        Projects, on_delete=models.CASCADE, blank=True, null=True, default=None)
    created_date = models.DateField(auto_now_add=True)

    @property
    def formatted_markdown(self):
        return markdownify(self.markdownFile)

    def get_absolute_url(self):
        return reverse('markdown-detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.title
