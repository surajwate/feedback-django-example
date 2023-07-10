from django.urls import path
from . import views

urlpatterns = [
    path('', views.ReviewView.as_view()),
    path('thank_you', views.ThankYouView.as_view()),
    path('reviews', views.ReviewListView.as_view()),
]
