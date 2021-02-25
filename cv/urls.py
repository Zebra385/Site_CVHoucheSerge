from .views import AccueilView
from django.urls import path, include

app_name = "cv"

urlpatterns = [
    path('accueil/', AccueilView.as_view(), name="accueil"),
   
]
