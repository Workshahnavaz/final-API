from django.contrib import admin
from django.urls import path,include

from.views import *

urlpatterns = [
    path('',Chat),
    path('post/',info),
    path('put/<id>/',details),
    path('patch/<id>/',database),
    path('delete/<id>/',metter)

]
