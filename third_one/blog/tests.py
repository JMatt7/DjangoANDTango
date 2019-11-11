from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse
from .models import Post
# Create your tests here.

class BlogTests(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username = 'test user',
            email = 'test@email.com',
            password = 'secret',
        )

        self.post = Post.objects.create(
            author = self.user,
            title = 'sample title',
            body = 'sample text',
        )
    
    def string_representation(self):
        post = Post(title = 'good title')
        self.assertEqual(str(post), post.title)

    def test_get_absolute_url(self):
        self.assertEqual(self.post.get_absolute_url(), '/post/1/')

    def test_post_content(self):
        self.assertEqual(f'{self.post.author}', 'test user')
        self.assertEqual(f'{self.post.title}', 'sample title')
        self.assertEqual(f'{self.post.body}', 'sample text')

    def test_post_list_view(self):
        resp = self.client.get(reverse('home'))
        self.assertEqual(resp.status_code, 200)
        self.assertContains(resp, 'sample title')
        self.assertTemplateUsed(resp, 'home.html')

    def test_post_detail_view(self):
        resp = self.client.get('/post/1/')
        no_resp = self.client.get('/post/100000/')
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(no_resp.status_code, 404)
        self.assertContains(resp, 'sample title')
        self.assertTemplateUsed(resp, 'post_detail.html')

    def test_post_create_view(self):
        resp = self.client.post(reverse('post_new'),{
            'title' : 'new title',
            'body' : 'new body',
            'author' : self.user,


        })
        self.assertEqual(resp.status_code, 200)
        self.assertContains(resp, 'new title')
        self.assertContains(resp, 'new body')

    def test_post_edit_view(self):
        resp = self.client.post(reverse('post_edit', args = "1"), {
            'title' : 'updated title',
            'body' : 'updated body',    
        })
        self.assertEqual(resp.status_code, 302)

    def test_post_delete_view(self):
        resp = self.client.get(reverse('post_delete', args = "1"), {
            'title' : 'updated title',
            'body' : 'updated body',    
        })
        self.assertEqual(resp.status_code, 200)

