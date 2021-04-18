from django.urls import path


from .views import *

app_name = "accueil"
from . import views


urlpatterns = [
#    path('edit-profile', ProfileEditView.as_view(), name="edit-profile"),
    path('accueil/', views.AccueilView, name="accueil"),
]