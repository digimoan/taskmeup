"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from task.views import home_view, tracker_view, createPage_view, projectPage_view, taskPage_view, projectPageTask_view,\
    projectPageRoadmap_view, taskPagedone_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view.as_view(), name='index'),
    path('home/', home_view.as_view(), name='home'),
    path('timetracker/', tracker_view.as_view(), name='tracker'),
    path('create/', createPage_view.as_view(), name='createPage'),
    path('project/', projectPage_view.as_view(), name='projectPage'),
    path('tasks/', taskPage_view.as_view(), name='taskPage'),
    path('tasks1/', taskPagedone_view.as_view(), name='taskPagedone'),
    path('project_tasks/', projectPageTask_view.as_view(), name='projectTaskPage'),
    path('roadmap/', projectPageRoadmap_view.as_view(), name='projectPageRoadmap'),
]
