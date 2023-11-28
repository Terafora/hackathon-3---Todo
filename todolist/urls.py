from django.urls import path
from .views import Home, CreateNote, NoteDetail, DeleteNote

urlpatterns = [
    path('', Home.as_view(), name="home"),
    path('createnote/', CreateNote.as_view(), name="create_note"),
    path('<slug:pk>/', NoteDetail.as_view(), name="note_detail"),
    path('<slug:pk>/', NoteDelete.as_view(), name="note_delete"),
]
