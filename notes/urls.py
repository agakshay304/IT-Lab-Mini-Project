from django.urls import path
from . import views

urlpatterns = [
    path('list', views.NotesListView.as_view(), name="notes.list"),
    path('detail/<int:pk>',views.NoteDetailView.as_view(), name="notes.detail"),
    path('edit/<int:pk>',views.NotesUpdateView.as_view(), name="notes.update"),
    path('delete/<int:pk>',views.NotesDeleteView.as_view(), name="notes.delete"),
    path('new',views.NotesCreateView.as_view(), name="notes.new"),
    path('file/<int:pk>',views.FileView.as_view(), name="notes.file"),
]
