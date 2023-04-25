from django.shortcuts import render
from django.http.response import HttpResponseRedirect
from django.views.generic import CreateView,DetailView,ListView,UpdateView
from django.views.generic.edit import DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Notes
from .forms import NoteForm

# Create your views here.

class NotesCreateView(LoginRequiredMixin,CreateView):
    model = Notes
    # fields = ['title','text']
    form_class = NoteForm
    success_url = '/notes/list'
    template_name = "notes/notes_form.html"
    login_url = "/login"
    
    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())

    
class NotesUpdateView(LoginRequiredMixin,UpdateView):
    model = Notes
    form_class = NoteForm
    success_url = '/notes/list'
    template_name = "notes/notes_form.html"
    login_url = "/login"
    
class NotesListView(LoginRequiredMixin,ListView):
    model = Notes
    context_object_name = 'notes'
    template_name = 'notes/notes_list.html'
    login_url = "/login"
    
    def get_queryset(self):
        return self.request.user.notes.all()
    
class NoteDetailView(LoginRequiredMixin,DetailView):
    model = Notes
    context_object_name = 'note'
    template_name = 'notes/notes_detail.html'
    login_url = "/login"
    
class NotesDeleteView(LoginRequiredMixin,DeleteView):
    model = Notes
    success_url = '/notes/list'
    template_name = "notes/notes_delete.html"
    login_url = "/login"

# Class to view the uploaded file
class FileView(LoginRequiredMixin, DetailView):
    model = Notes
    template_name = 'notes/file.html'
    login_url = "/login"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['file'] = self.object.file
        return context





# class NotesCreateView(LoginRequiredMixin, CreateView):
#     model = Notes
#     form_class = NoteForm
#     success_url = '/notes/list'
#     template_name = "notes/notes_form.html"
#     login_url = "/login"
    
#     def form_valid(self, form):
#         self.object = form.save(commit=False)
#         self.object.user = self.request.user
        
#         # Save the uploaded file
#         self.object.image = self.request.FILES.get('image')
        
#         self.object.save()
#         return HttpResponseRedirect(self.get_success_url())
