from django.urls import path


from .views import *

app_name = "profile"
from . import views


urlpatterns = [
#    path('edit-profile', ProfileEditView.as_view(), name="edit-profile"),
    path('user-profile/', views.getprofileData, name="user-profile"),

]
