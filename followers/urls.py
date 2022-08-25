from django.urls import path
from followers import views

urlpatterns = [
    path('follower/', views.Followerview.as_view()),
    path('follower/<int:pk>/', views.FollowerDetail.as_view()),
]