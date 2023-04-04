from django.urls import path
from . import views
urlpatterns = [
    path('',views.home, name = "home"),
    path('room/<slug:pk>', views.room, name ="room"),
    path('login/', views.loginPage, name = "login"),
    path('logout/', views.logoutPage, name = "logout"),
    path('register/', views.registerPage, name = "register"),
    path('profile/<slug:pk>', views.userProfile, name = "profile"),
    path('create-room/', views.createRoom, name = "create-room"),
    path('update-room/<slug:pk>', views.updateRoom, name = "update-room"),
    path('delete-room/<slug:pk>', views.deleteRoom, name = "delete-room"),
    path('delete-message/<slug:pk>', views.deleteMessage, name = "delete-message"),


]
