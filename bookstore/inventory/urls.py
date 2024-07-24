from django.urls import path
from . import views

urlpatterns = [
    path('',views.home_page,name="home_page"),
    path('books/',views.list_books,name="list_books"),
    path('books/<int:book_id>/',views.book_detail,name="book_detail"),
    path('books/new/',views.create_book,name="create_book"),
    path('book/edit/<int:book_id>/',views.edit_book,name="edit_book"),
    path('book/delete/<int:book_id>/',views.delete_book,name="delete_book")
]