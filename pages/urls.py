from django.urls import path
from pages import views as pages_views

urlpatterns= [
    path("", pages_views.home.as_view(), name="home"),
    path("about/", pages_views.about.as_view(), name="about")
]