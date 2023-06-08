from django.urls import path
from . import views

app_name = "core"

urlpatterns = [
    path('', views.index, name="home"),
    path('signup/', views.signup, name="signup"),
    path('login/', views.login, name="login"),

]