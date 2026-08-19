from django import forms
from .models import Post, Author

class PostForm(forms.ModelForm):
    """
    Form for creating and updating Post instances.
    """
    class Meta:
        model = Post
        fields = ['title', 'content', 'author']


class AuthorForm(forms.ModelForm):
    """
    Form for creating new Author instances.
    """
    class Meta:
        model = Author
        fields = ['name']