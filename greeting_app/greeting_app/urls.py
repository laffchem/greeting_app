"""
URLs for greeting_app.
"""
from django.urls import path  # pylint: disable=unused-import
from django.views.generic import TemplateView  # pylint: disable=unused-import
from .views import greeting


urlpatterns = [
    path("greeting/", greeting, name="greeting-api")
]
