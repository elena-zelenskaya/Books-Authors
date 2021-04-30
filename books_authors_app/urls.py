from django.urls import path
from . import views

urlpatterns = [
    path("", views.index),
    path("books/", views.show_books),
    path("books/add_book/", views.add_book),
    path("books/<int:number>/", views.view_book),
    path("books/delete/<int:number>/", views.delete_book),
    path("authors/", views.show_authors),
    path("authors/add_author/", views.add_author),
    path("authors/<int:number>/", views.view_author),
    path("authors/delete/<int:number>/", views.delete_author),
    path("books/<int:number>/select/", views.select_author),
    path("books/<int:book_id>/delete/<int:author_id>/", views.delete_author_from_book),
    path("authors/<int:number>/select/", views.select_book),
    path("authors/<int:author_id>/delete/<int:book_id>/", views.delete_book_from_author),
]