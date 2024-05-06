from django.test import SimpleTestCase
from django.urls import reverse, resolve
from .views import HomepageView, AboutPageView, IndexPageView

# Create your tests here.
class HomepageTests(SimpleTestCase):
    """Tests that homepage renders correctly"""

    def setUp(self):
        url = reverse('home')
        self.response = self.client.get(url)

    def test_homepage_status_code(self):
        self.assertEqual(self.response.status_code, 200)

    def test_homepage_template(self):
        self.assertTemplateUsed(self.response, 'home.html')

    def test_homepage_contains_correct_html(self):
        self.assertContains(self.response, 'Homepage')

    def test_homepage_does_not_contain_incorrect_html(self):
        self.assertNotContains(self.response, 'Hi there, I should not be on the page')

    def test_homepage_url_resolves_homepage_view(self):
        view = resolve('/')
        self.assertEqual(
                view.func.__name__, HomepageView.as_view().__name__
                )

class AboutPageTests(SimpleTestCase):
    """Tests that about page renders correctly"""
    def setUp(self):
        url = reverse('about')
        self.response = self.client.get(url)

    def test_about_page_status_code(self):
        self.assertEqual(self.response.status_code, 200)

    def test_about_page_template(self):
        self.assertTemplateUsed(self.response, 'about.html')

    def test_about_page_contains_correct_html(self):
        self.assertContains(self.response, 'About page')

    def test_about_page_does_not_contain_incorrect_html(self):
        self.assertNotContains(self.response, 'Hi there, I should not be on the page')

    def test_about_page_url_resolves_about_view(self):
        view = resolve('/about/')
        self.assertEqual(
                view.func.__name__, AboutPageView.as_view().__name__
                )

class IndexPageTests(SimpleTestCase):
    """Tests that index page renders correctly"""
    def setUp(self):
        url = reverse('index')
        self.response = self.client.get(url)

    def test_index_page_status_code(self):
        self.assertEqual(self.response.status_code, 200)

    def test_index_page_template(self):
        self.assertTemplateUsed(self.response, 'index.html')

    def test_index_page_contains_correct_html(self):
        self.assertContains(self.response, 'Books: The Original Escape Room')

    def test_index_page_does_not_contain_incorrect_html(self):
        self.assertNotContains(self.response, 'Hi, I should not be on this page')

    def test_index_page_url_resolves_index_view(self):
        view = resolve('/index/')
        self.assertEqual(
                view.func.__name__, IndexPageView.as_view().__name__
                )
