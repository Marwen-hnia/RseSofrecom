from django.urls import path


from .views import *

app_name = "listamis"
from . import views


urlpatterns = [
#    path('edit-profile', ProfileEditView.as_view(), name="edit-profile"),
    path('amis/', views.AmisView, name="amis"),

]