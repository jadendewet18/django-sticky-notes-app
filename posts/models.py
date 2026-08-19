from django.db import models

class Author(models.Model):
    """
    Represents an author who creates sticky notes.
    """
    name = models.CharField(max_length=100)

    def __str__(self):
        """Return the author's name as string representation."""
        return self.name


class Post(models.Model):
    """
    Represents an individual sticky note post created by an author.
    """
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, default=1, related_name='posts')

    def __str__(self):
        """Return the post title as string representation."""
        return self.title