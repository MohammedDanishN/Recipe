from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

from .views import *
urlpatterns = [
    path('', student, name='home'),
    path('marks/<id>', marks, name='marks',)
]
