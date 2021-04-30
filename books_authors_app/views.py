from django.shortcuts import render, redirect
from .models import Book, Author

# Create your views here.
def index(request):
    return render(request, "index.html")


def show_books(request):
    context = {"list_of_books": Book.objects.all()}
    return render(request, "books.html", context)


def add_book(request):
    if request.method == "POST":
        title = request.POST["book_title"]
        description = request.POST["book_description"]
        Book.objects.create(title=title, desc=description)
        return redirect("../")


def delete_book(request, number):
    book_to_delete = Book.objects.get(id=number)
    book_to_delete.delete()
    return redirect("../../")


def show_authors(request):
    context = {"list_of_authors": Author.objects.all()}
    return render(request, "authors.html", context)


def add_author(request):
    if request.method == "POST":
        first_name = request.POST["fname"]
        last_name = request.POST["lname"]
        notes = request.POST["notes"]
        Author.objects.create(first_name=first_name, last_name=last_name, notes=notes)
        return redirect("../")


def delete_author(request, number):
    author_to_delete = Author.objects.get(id=number)
    author_to_delete.delete()
    return redirect("../../")


def view_book(request, number):
    book_to_view = Book.objects.get(id=number)
    context = {"book_to_view": book_to_view, "authors": Author.objects.all()}
    return render(request, "book_info.html", context)


def view_author(request, number):
    author_to_view = Author.objects.get(id=number)
    context = {"author_to_view": author_to_view, "books": Book.objects.all()}
    return render(request, "author_info.html", context)


def select_author(request, number):
    if request.method == "POST":
        selected_author = request.POST["authors_list"]
        Book.objects.get(id=number).authors.add(Author.objects.get(id=selected_author))
        return redirect("../")

def delete_author_from_book(request, book_id, author_id):
    Book.objects.get(id=book_id).authors.remove(Author.objects.get(id=author_id))
    return redirect("../../")

def select_book(request, number):
    if request.method == "POST":
        selected_book = request.POST["books_list"]
        Author.objects.get(id=number).books.add(Book.objects.get(id=selected_book))
        return redirect("../")

def delete_book_from_author(request, book_id, author_id):
    Author.objects.get(id=author_id).books.remove(Book.objects.get(id=book_id))
    return redirect("../../")
