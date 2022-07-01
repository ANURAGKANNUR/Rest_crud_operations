from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from rest_framework.response import Response

from .models import Book
from .serializers import BookSerializer

# Create your views here.

@api_view(['GET'])
def api_overview(request):
    api_urls={
        'List':'book-list/',
        'Create':'add-book/',
        'Detail':'detail/<int:pk>',
        'Update':'update/<int:pk>',
        'delete':'deletebook/<int:pk>'
    }
    return Response(api_urls)
#list
@api_view(['GET'])
def booklist(request):
    book=Book.objects.all()
    serializer=BookSerializer(book,many=True)
    return Response(serializer.data)

#add book
@api_view(['POST'])
def addbook(request):
    serializer=BookSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


#view book
@api_view(['GET'])
def viewbook(request,pk):
    book=Book.objects.get(id=pk)
    serializer=BookSerializer(book,many=False)
    return Response(serializer.data)

#update
@api_view(['POST'])
def update(request,pk):
    book=Book.objects.get(id=pk)
    serializer=BookSerializer(instance=book,data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

#delete
@api_view(['GET'])
def deletebook(request,pk):
    book=Book.objects.get(id=pk)
    book.delete()
    return Response("Book has been Removed ")