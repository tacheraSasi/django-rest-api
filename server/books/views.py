from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from .models import Book
from django.core import serializers
import json

# Create your views here.

@csrf_exempt
@require_http_methods(["GET","POST"])
def index(request):
    if request.method == "GET":
        books  = Book.objects.all()
        # data = serializers.serialize("json",book)
        data = [{'id': book.id, 'title': book.title, 'author': book.author} for book in books]
        return JsonResponse(data, safe=False, content_type = "application/json")
    elif request.method == "POST":
        try:
            data = json.loads(request.body)
            print(request.body)
            if data == None:
                return JsonResponse({"error":"Body is empty"},status = 400)
            
            title = data["title"]
            author = data["author"]
            book = Book.objects.create(
                title = title,
                author = author
            )
            JsonResponse(
                {
                    'id':book.id,
                    'title':book.title,
                    'author':book.author
                },
                status = 201
            )
        except KeyError:
            return JsonResponse({"error":"invalid request"},status = 400)

