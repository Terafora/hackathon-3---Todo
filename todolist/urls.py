from django.urls import path
from .views import Home, CreateNote, NoteDetail, DeleteNote, EditNote, about

urlpatterns = [
    path('', Home.as_view(), name="home"),
    path('about/', about, name='about'),
    path('createnote/', CreateNote.as_view(), name="create_note"),
    path('<slug:slug>/', NoteDetail.as_view(), name="note_detail"),
    path('delete/<slug:slug>/', DeleteNote.as_view(), name="note_delete"),
    path('edit/<slug:slug>/', EditNote.as_view(), name="note_edit"),
]
