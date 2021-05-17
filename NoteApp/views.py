from .forms import NoteForm
from django.shortcuts import render, redirect
import logging

from .models import Notes, Category

logger = logging.getLogger(__name__)


def index(request):

    form = "Welcome"

    return render(request, 'home.html', {'form': form})


def make_note(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/home/', id=form)
    else:
        form = NoteForm()
    return render(request, 'create_note.html', {'form': form})


def list_note(request):
    form = Notes.objects.all()
    return render(request, 'display_note.html', {'form': form})


def contact(request):
    form = "contact us"
    return render(request, 'contact.html', {'form': form})