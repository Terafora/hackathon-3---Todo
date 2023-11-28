from django.views.generic import TemplateView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Note
from .forms import NoteForm

# Create your views here.

class Home(TemplateView):
    template_name = "todolist/index.html"


class CreateNote(LoginRequiredMixin, CreateView):
    """Add a new note"""
    template_name = "todolist/create_note.html"
    model = Note
    success_url = ""

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(CreateNote, self).form_valid(form)