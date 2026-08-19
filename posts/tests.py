from django.test import TestCase
from django.urls import reverse
from .models import Post, Author


class PostModelTest(TestCase):
    """Unit tests for the Post model."""

    def setUp(self):
        """Set up test data for model tests."""
        author = Author.objects.create(name='Test Author')
        Post.objects.create(
            title='Test Post',
            content='This is a test post.',
            author=author
        )

    def test_post_has_title(self):
        """Test that a Post object retains the expected title."""
        post = Post.objects.get(id=1)
        self.assertEqual(post.title, 'Test Post')

    def test_post_has_content(self):
        """Test that a Post object retains the expected content."""
        post = Post.objects.get(id=1)
        self.assertEqual(post.content, 'This is a test post.')


class PostViewTest(TestCase):
    """Unit tests for Post views."""

    def setUp(self):
        """Set up test data for view tests."""
        author = Author.objects.create(name='Test Author')
        Post.objects.create(
            title='Test Post',
            content='This is a test post.',
            author=author
        )

    def test_post_list_view(self):
        """Test the post list view response status and content."""
        response = self.client.get(reverse('post_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Post')

    def test_post_detail_view(self):
        """Test the post detail view response status and content."""
        post = Post.objects.get(id=1)
        response = self.client.get(reverse('post_detail', args=[str(post.id)]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Post')
        self.assertContains(response, 'This is a test post.')