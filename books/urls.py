from django.urls import path
from .views import about_view,time_view,hobbies_view


urlpatterns = [
    path('about/', about_view, name='about'),
    path('time/', time_view, name='time'),
    path('hobbies/', hobbies_view, name='hobbies')
]