from django.urls import path
from .views import HomepageView, AboutPageView

urlpatterns = [
        # Home page
        path('', HomepageView.as_view(), name='home'),

        # About page
        path('about/', AboutPageView.as_view(), name='about'),
    ]
