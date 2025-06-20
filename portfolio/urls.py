from __future__ import unicode_literals

from django.urls import re_path
from django.views.generic.list import ListView

from .models import Project


urlpatterns = [
    re_path(
        r"^$",
        ListView.as_view(
            context_object_name="project", queryset=Project.objects.published()
        ),
        name="portfolio-project-list",
    ),
]
