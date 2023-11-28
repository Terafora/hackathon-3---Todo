from django.urls import path
from .views import Home, CreateNote

urlpatterns = [
    path('', Home.as_view(), name="home"),
    path('createnote', CreateNote.as_view(), name="create_note"),

]
