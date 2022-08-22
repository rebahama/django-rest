from django.urls import path
from profiles_drf import views


urlpatterns = [
    path('profiles/', views.ProfileList.as_view()),
]