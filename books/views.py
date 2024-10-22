from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Book
from .serializers import BookSerializer
from django.http import Http404
from rest_framework.pagination import PageNumberPagination
from django_filters import rest_framework as filters


class BookPagination(PageNumberPagination):
    page_size = 10


class BookFilter(filters.FilterSet):
    """ filter for filtering books by author and language."""
    author = filters.CharFilter(field_name='author', lookup_expr='icontains')  # Partial match
    language = filters.CharFilter(field_name='language', lookup_expr='icontains')  # Partial match


    class Meta:
        model = Book
        fields = ['author', 'language']


class BookListCreate(APIView):
    """Handles GET request for books with pagination and filtering."""

    def get(self, request):
        """ Get all books from db and return them as a JSON response."""

        books = Book.objects.all()
        filterset = BookFilter(request.GET, queryset=books)
        if filterset.is_valid():
            books = filterset.qs

        paginator = BookPagination()
        paginated_books = paginator.paginate_queryset(books, request)
        serializer = BookSerializer(paginated_books, many=True)

        return paginator.get_paginated_response(serializer.data)

    def post(self, request):
        """ Create new book in db using data in the request."""
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class BookDetail(APIView):
    """ Handles GET, PUT, and DELETE requests for individual books. """
    def get(self, request, id):
        """Get details of book by ID."""
        try:
            book = Book.objects.get(pk=id)
        except Book.DoesNotExist:
            raise Http404("Book not found.")
        serializer = BookSerializer(book)
        return Response(serializer.data)

    def put(self, request, id):
        """Update details of book."""
        try:
            book = Book.objects.get(pk=id)
        except Book.DoesNotExist:
            raise Http404("Book not found.")
        serializer = BookSerializer(book, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        """
        Delete book from db."""
        try:
            book = Book.objects.get(pk=id)
        except Book.DoesNotExist:
            raise Http404("Book not found.")
        book.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
