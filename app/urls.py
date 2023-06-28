from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

from .views import *
urlpatterns = [
    path('', home, name='home'),
    path('create/', create_recipe, name='create_recipe'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('register/', register, name='register'),
    path('delete/<int:id>', delete_recipe, name='delete_recipe'),
    path('update/<int:id>', update_recipe, name='update_recipe'),
]
