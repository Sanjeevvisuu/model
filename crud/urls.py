from django.contrib import admin
from django.urls import path
from .views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path("",home,name="home"),
    path("create_new_student",create,name="create_new_student"),
    path("update/<int:id>/", update, name="update"),

    path("delete/<int:id>/",delete,name="delete"),
]
