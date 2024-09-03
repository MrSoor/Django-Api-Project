from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *
from .serializers import *
# Create your views here.
class BookApiView(APIView):
    serializer_class=BookSerializer
    def get(self,request):
        allBooks=Book.objects.all().values()
        return Response({"Message":"List of Books", "Book List":allBooks})

    def post(self,request):
        print('Request data is : ',request.data)
        serializer_obj=BookSerializer(data=request.data)
        if(serializer_obj.is_valid()):
        
            Book.objects.create(id=serializer_obj.data.get("id"),
                            title=serializer_obj.data.get("title"),
                            author=serializer_obj.data.get("author"))
        
        book=Book.objects.all().filter(id=request.data["id"]).values()
        return Response({"Message":"New Book Added!", "Book":book})
    
class ProductApiView(APIView):
    serializer_class=ProductSerializer
    def get(self,request):
        allproduct=Product.objects.all().values()
        return Response({"Message":"List of product", "product List":allproduct})

    def post(self,request):
        print('Request data is : ',request.data)
        serializer_obj=ProductSerializer(data=request.data)
        if(serializer_obj.is_valid()):
        
            Product.objects.create(product_name=serializer_obj.data.get("product_name"),
                            category=serializer_obj.data.get("category"),
                            subcategory=serializer_obj.data.get("subcategory"),
                            price=serializer_obj.data.get("price"),
                            desc=serializer_obj.data.get("desc")),
        
        product=Product.objects.all().filter(product_name=request.data["product_name"]).values()
        return Response({"Message":"New product Added!", "product":product})
    