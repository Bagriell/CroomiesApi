"""croomies URL Configuration

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
from django.urls import path, include
from rest_framework import routers
from croomies_api import views
from knox import views as knox_views



router = routers.DefaultRouter()
router.register(r'address', views.AddressView)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/register/', views.RegisterAPI.as_view(), name='register'),
    path('api/login/', views.LoginAPI.as_view(), name='login'),
    path('api/logout/', knox_views.LogoutView.as_view(), name='logout'),
    path('api/logoutall/', knox_views.LogoutAllView.as_view(), name='logoutall'),
    path('api/habitation/', views.HabitationAPI.as_view(), name='Habitations'),
    path('api/sport/', views.SportAPI.as_view(), name='Sport'),
    path('api/film/', views.FilmAPI.as_view(), name='Film'),
    path('api/music/', views.MusicAPI.as_view(), name='Music'),
    path('api/sport_user/', views.Sport_userAPI.as_view(), name='Sport_user'),
    path('api/film_user/', views.Film_userAPI.as_view(), name='Film_user'),
    path('api/music_user/', views.Music_userAPI.as_view(), name='Music_user'),
    path('api/media/', views.MediaAPI.as_view(), name='Media'),
    path('api/address/', views.AddressAPI.as_view(), name='Address'),
    path('api/croomiesUser/', views.CroomiesUserAPI.as_view(), name='CroomiesUser'),
    path('api/seeker/', views.SeekerAPI.as_view(), name='Seeker'),
    path('api/matching/', views.MatchingAPI.as_view(), name='Matching'),
    path('api/roomate_in_habitation/', views.Roomate_in_habitationAPI.as_view(), name='Roomate_in_habitation'),
    path('api/media_habitation/', views.Media_habitationAPI.as_view(), name='Media_habitation'),
    path('api/time_slots/', views.Time_slotsAPI.as_view(), name='Time_slots'),
    path('api/date_slots/', views.Date_slotsAPI.as_view(), name='Date_slots'),
    path('api/visite/', views.VisiteAPI.as_view(), name='Visite'),
    path('api/application/', views.ApplicationAPI.as_view(), name='Application')

]