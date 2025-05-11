from django.urls import path
from .views import *



urlpatterns = [
    path('<str:lng>/', home, name="home"),
    path('<str:lng>/pages/<slug:custom_url>', dynamic_page, name="dynamic_page"),
    path('', base_home, name="home"),
    path('html/<str:slug>', return_html_page, name="return_html_page"),


]
