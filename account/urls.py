from django.urls import path

from account.views import AccueilView

urlpatterns = [
    path('', AccueilView.as_view(), name='accueil'),
]