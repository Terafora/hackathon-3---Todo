from django.views.generic import ListView, CreateView, DetailView, DeleteView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Note
from .forms import NoteForm

# Create your views here.

class Home(ListView):
    """View all to do notes on home page"""
    template_name = "todolist/index.html"
    model = Note
    context_object_name = 'note_board'
    
class NoteDetail(DetailView):
    """Show details of one note"""
    template_name = "todolist/note_detail.html"
    model = Note
    context_object_name = "note"


class CreateNote(LoginRequiredMixin, CreateView):
    """Add a new note"""
    template_name = "todolist/create_note.html"
    model = Note
    form_class = NoteForm
    success_url = ""

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(CreateNote, self).form_valid(form)

class EditNote(LoginRequiredMixin, UserPassesTestMixin ,UpdateView):
    """Update a note"""
    template_name = "todolist/note_edit.html"
    model = Note
    form_class = NoteForm 
    success_url = ""

    def test_func(self):
        return self.request.user == self.get_object().user

class DeleteNote(LoginRequiredMixin, UserPassesTestMixin ,DeleteView):
    """Delete a note"""
    model = Note
    success_url = ""

    def test_func(self):
        return self.request.user == self.get_object().user