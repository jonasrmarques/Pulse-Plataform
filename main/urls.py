from django.urls import path
from .views import HomeView, PrincipalPageView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('principal-page/', PrincipalPageView.as_view(), name='principal-page')
]