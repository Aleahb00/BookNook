from django.shortcuts import render, redirect, get_object_or_404
from django.http.request import HttpRequest
from django.http.response import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from django.contrib.auth.models import Group
from .models import *
from .forms import *

# Create your views here.
def landing_view(request: HttpRequest) -> HttpResponse:
    return render(request, 'landing.html')


def register_view(request):
        if request.method == 'POST':
            form = RegistrationForm(request.POST)
            if form.is_valid():
                user = form.save()
                group = Group.objects.get(name='members')
                user.groups.add(group)
                return redirect('login')
        else:
            form = RegistrationForm()
        return render(request, 'registration.html', {'form': form})


def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            if user.groups.filter(name="owner").exists():
                return redirect("owner_dashboard")
            return redirect("home")
    else:
        form = AuthenticationForm()
    return render(request, "login.html", {"form": form})



@login_required

def logout_view(request:HttpRequest)->HttpResponse:
    logout(request)
    return redirect('landing')


def home_view(request, category=None):
    books = Book.objects.filter(
        bookshelves__user=request.user
    ).distinct()
    if category:
        books = books.filter(category__iexact=category)
    bookshelves = Bookshelf.objects.filter(user=request.user)
    return render(request, "home.html", {
        "books": books,
        "active_category": category,
        "bookshelves": bookshelves
    })
    
def shelf_view(request):
    bookshelves = Bookshelf.objects.filter(user=request.user)
    return render(request, "shelf_view.html", {"bookshelves": bookshelves})

def add_book_view(request):
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            book = form.save()
            return redirect("home")
    else:
        form = BookForm()
    form.fields["bookshelves"].queryset = Bookshelf.objects.filter(
        user=request.user
    )
    return render(request, "add_book.html", {"form": form})

def add_shelf_view(request):
    if request.method == "POST":
        form = BookshelfForm(request.POST)
        if form.is_valid():
            new_shelf = form.save(commit=False)
            new_shelf.user = request.user
            new_shelf.save()
            return redirect('home')
    else:
        form = BookshelfForm()
    return render(request, 'add_shelf.html', {'form': form})

def edit_book_view(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if not book.bookshelves.filter(user=request.user).exists():
        return HttpResponseForbidden()
    form = BookForm(request.POST or None, instance=book)
    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect("home")
    return render(request, "edit_book.html", {"form": form})

def edit_shelf_view(request, shelf_id):
    shelf = get_object_or_404(Bookshelf, id=shelf_id, user=request.user)
    form = BookshelfForm(request.POST or None, instance=shelf)
    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect("shelf_view")
    return render(request, "edit_shelf.html", {"form": form})

def delete_book_view(request, book_id):
    book = get_object_or_404(Book, id=book_id, bookshelves__user=request.user)
    if request.method == "POST":
        book.delete()
        return redirect("home")
    return render(request, "home.html", {"object": book, "type": "book"})

def delete_shelf_view(request, shelf_id):
    shelf = get_object_or_404(Bookshelf, id=shelf_id, user=request.user)
    if request.method == "POST":
        shelf.delete()
        return redirect("shelf_view")
    return render(request, "home.html", {"object": shelf, "type": "shelf"})




def owner_dashboard_view(request):
    users = User.objects.exclude(username__in=["owner","admin"])
    books = Book.objects.all()
    shelves = Bookshelf.objects.all()
    return render(request, "owner_dashboard.html", {
        "users": users,
        "books": books,
        "shelves": shelves,
    })


def owner_edit_book_view(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    form = BookForm(request.POST or None, instance=book)
    if form.is_valid():
        form.save()
        return redirect("owner_dashboard")
    return render(request, "owner_edit_book.html", {"form": form})


def owner_edit_shelf_view(request, shelf_id):
    shelf = get_object_or_404(Bookshelf, id=shelf_id)
    form = BookshelfForm(request.POST or None, instance=shelf)
    if form.is_valid():
        form.save()
        return redirect("owner_dashboard")
    return render(request, "owner_edit_shelf.html", {"form": form})


def owner_delete_book_view(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == "POST":
        book.delete()
        return redirect("owner_dashboard")
    return render(request, "owner_dashboard.html", {"object": book, "type": "book"})


def owner_delete_shelf_view(request, shelf_id):
    shelf = get_object_or_404(Bookshelf, id=shelf_id)
    if request.method == "POST":
        shelf.delete()
        return redirect("owner_dashboard")
    return render(request, "owner_dashboard.html", {"object": shelf, "type": "shelf"})


def owner_delete_user_view(request, user_id):
    user = get_object_or_404(User, id=user_id)
    if request.method == "POST":
        user.delete()
        return redirect("owner_dashboard")
    return render(request, "owner_dashboard.html", {"object": user, "type": "user"})