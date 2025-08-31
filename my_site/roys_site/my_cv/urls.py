from django.urls import path

from . import views

urlpatterns = [
    path("", views.cv_page, name="cv_page"),
    # path("job_desc_page/", views.job_desc_page, name="job_desc_page")
    path("<slug:slug>", views.job_desc_page, name="job_desc_page")
]