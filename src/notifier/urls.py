from django.urls import path

from src.notifier.views import HomeView

urlpatterns = [
    path('', HomeView.as_view(), name="index"),
]
