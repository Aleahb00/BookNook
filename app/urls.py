from django.urls import path
from .views import *

urlpatterns = [
    path('', landing_view, name='landing'),
    path('home/', home_view, name='home'),
    path("category/<str:category>/", home_view, name="books_filtered"),
    path('home/shelf/', shelf_view, name='shelf_view'),
    path('home/book/add/', add_book_view, name='add_book'),
    path('home/shelf/add/', add_shelf_view, name='add_shelf'),
    path("book/edit/<int:book_id>/", edit_book_view, name="edit_book"),
    path("shelf/edit/<int:shelf_id>/", edit_shelf_view, name="edit_shelf"),
    path("book/delete/<int:book_id>/", delete_book_view, name="delete_book"),
    path("shelf/delete/<int:shelf_id>/", delete_shelf_view, name="delete_shelf"),
    path("owner/", owner_dashboard_view, name="owner_dashboard"),
    path("owner/book/<int:book_id>/", owner_edit_book_view, name="owner_edit_book"),
    path("owner/shelf/<int:shelf_id>/", owner_edit_shelf_view, name="owner_edit_shelf"),
    path("owner/book/<int:book_id>/delete", owner_delete_book_view, name="owner_delete_book"),
    path("owner/shelf/<int:shelf_id>/delete", owner_delete_shelf_view, name="owner_delete_shelf"),
    path("owner/user/<int:user_id>/", owner_delete_user_view, name="owner_delete_user"),
    path('register/', register_view, name="register"),
    path('login/', login_view, name="login"),
    path('logout/', logout_view, name="logout"),
]