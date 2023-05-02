from django.shortcuts import render
from django.http import Http404
from .models import Notes
from django.views.generic import CreateView, ListView, DetailView

class NotesCreateView(CreateView):
    model = Notes
    fields = ['title', 'text']
    success_url = '/smart/notes'

class NotesListView(ListView):
    model = Notes
    context_object_name = "notes"
    template_name = 'notes/notes_list.html'
    
class NotesDetailView(DetailView):
    model = Notes
    context_object_name = "note"