from django.contrib.auth.forms import UserCreationForm
from django.db import models
from django.urls import reverse


class Watch(models.Model):
    name = models.CharField(max_length=250)
    author = models.ForeignKey(
        'auth.User',
        on_delete=models.CASCADE,
    )
    description = models.TextField()
    link = models.URLField(max_length=250)
    finished = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('watch', args=[str(self.id)])


class UserCreateForm(UserCreationForm):

    def __init__(self, *args, **kwargs):
        super(UserCreateForm, self).__init__(*args, **kwargs)

        for field in ['username', 'password1', 'password2']:
            self.fields[field].help_text = None
