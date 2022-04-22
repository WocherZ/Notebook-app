from django.shortcuts import render, get_object_or_404
from django.views.generic import UpdateView, DeleteView

from .models import Note


def home(request):
    return render(request, "home.html")


def notes_list(request):
    context = {'notes': []}
    for note_object in Note.objects.all():
        context['notes'].append({
            'name': note_object.name,
            'date': note_object.date_published,
            'slug': note_object.slug
        })
    return render(request, "notes_list.html", context=context)


def note(request, note_slug):
    context = {}
    note_object = get_object_or_404(Note, slug=note_slug)
    context['name'] = note_object.name
    context['text'] = note_object.text
    context['date'] = note_object.date_published
    context['link_update'] = "/note/" + str(note_slug) + "/update/"
    context['link_delete'] = "/note/" + str(note_slug) + "/delete/"
    return render(request, "note.html", context=context)


class UpdateNote(UpdateView):
    model = Note
    template_name = "update_note.html"
    fields = ['name', 'text', 'date_published']


class DeleteNote(DeleteView):
    model = Note
    template_name = "delete_note.html"
    success_url = "/notes/"
