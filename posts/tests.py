from django.test import TestCase
from django.urls import reverse
from .models import Author, Post


class AuthorModelTest(TestCase):

    def setUp(self):
        self.author = Author.objects.create(name="Test Author")

    def test_author_creation(self):
        self.assertEqual(self.author.name, "Test Author")
        self.assertEqual(str(self.author), "Test Author")

    def test_author_create_view(self):
        response = self.client.post(reverse('author_create'), {'name': 'New Author'})
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Author.objects.filter(name='New Author').exists())


class PostModelAndCRUDTest(TestCase):

    def setUp(self):
        self.author = Author.objects.create(name="Jane Doe")
        self.post = Post.objects.create(
            title="Test Post",
            content="This is test content.",
            author=self.author
        )

    def test_post_creation(self):
        self.assertEqual(self.post.title, "Test Post")
        self.assertEqual(self.post.content, "This is test content.")
        self.assertEqual(self.post.author.name, "Jane Doe")
        self.assertEqual(str(self.post), "Test Post")

    def test_post_list_view(self):
        response = self.client.get(reverse('post_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Post")

    def test_post_detail_view(self):
        response = self.client.get(reverse('post_detail', args=[self.post.id]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "This is test content.")

    def test_post_create_view(self):
        response = self.client.post(reverse('post_create'), {
            'title': 'New Note',
            'content': 'Created via post view',
            'author': self.author.id
        })
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Post.objects.filter(title='New Note').exists())

    def test_post_update_view(self):
        response = self.client.post(reverse('post_update', args=[self.post.id]), {
            'title': 'Updated Title',
            'content': 'Updated content',
            'author': self.author.id
        })
        self.assertEqual(response.status_code, 302)
        self.post.refresh_from_db()
        self.assertEqual(self.post.title, 'Updated Title')

    def test_post_delete_view(self):
        response = self.client.post(reverse('post_delete', args=[self.post.id]))
        self.assertEqual(response.status_code, 302)
        self.assertFalse(Post.objects.filter(id=self.post.id).exists())