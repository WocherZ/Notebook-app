from django.shortcuts import render, get_object_or_404

from .models import Note


def home(request):
    return render(request, "home.html")


def notes_list(request):
    return render(request, "notes_list.html")


def note(request, note_slug):
    note_object = get_object_or_404(Note, slug=note_slug)
    return render(request, "note.html")


