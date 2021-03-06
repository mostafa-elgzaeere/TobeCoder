"""src URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from coder.views import show_tracks ,show_curses,show_current_video

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",show_tracks,name="show_tracks"),
    path("<int:track_id>/",show_curses,name="show_curses"),
    path("<int:track_id>/<int:curse_id>/",show_current_video,name="show_current_video")
]
