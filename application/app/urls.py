from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('notes/', views.notes_list, name="notes_list"),
    path('note/<slug:note_slug>/', views.note, name='note'),

    path('note/<slug:slug>/update/', views.UpdateNote.as_view(), name='update_note'),
]
