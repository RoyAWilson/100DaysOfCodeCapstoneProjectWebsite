from django.urls import path

from . import views

urlpatterns = [
    path("cv_page", views.cv_page, name="cv_page"),
]