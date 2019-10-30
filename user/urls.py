from django.urls import path
from user.views import user_home

urlpatterns = [
    path('', user_home, name="user_home"),
]
