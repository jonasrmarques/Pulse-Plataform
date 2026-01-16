from django.urls import path
from .views import UsersPageView

urlpatterns = [
    path("users/", UsersPageView.as_view(), name="users-page"),
]
