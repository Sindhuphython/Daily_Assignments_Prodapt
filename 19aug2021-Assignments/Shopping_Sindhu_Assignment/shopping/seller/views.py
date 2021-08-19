from django.shortcuts import render
from seller.models import Seller
from django.http.response import JsonResponse
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json
from seller.serializers import SellerSerializer
from rest_framework.parsers import JSONParser
from rest_framework import status

# Create your views here.
def seller_view(request):
    return render(request,'sin.html') 
@csrf_exempt
def seller_details(request,name):
    try:
        seller=Seller.objects.get(name=name)
        if(request.method=="GET"):
            seller_serializer=SellerSerializer(seller)
            return JsonResponse(seller_serializer.data,safe=False,status=status.HTTP_200_OK)
        if(request.method=="DELETE"):
            seller.delete()
            return HttpResponse("Delete",status=status.HTTP_204_NO_CONTENT)
        if(request.method=="PUT"):
            mydata=JSONParser().parse(request)
            seller_serialize=SellerSerializer(seller,data=mydata)
            if(seller_serialize.is_valid()):
                seller_serialize.save()
                return JsonResponse(seller_serialize.data,status=status.HTTP_200_OK)
            else:
                return JsonResponse(seller_serialize.errors,status=status.HTTP_400_BAD_REQUEST)
    except Seller.DoesNotExist:
        return HttpResponse("Invalid sellername",status=status.HTTP_404_NOT_FOUND)
@csrf_exempt
def seller_list(request):
    if(request.method=="GET"):
        sellers=Seller.objects.all()
        seller_serializer=SellerSerializer(sellers,many=True)
        return JsonResponse(seller_serializer.data,safe=False)
@csrf_exempt
def seller_create(request):
    if(request.method=="POST"):
        mydata=JSONParser().parse(request)
        seller_serialize=SellerSerializer(data=mydata)
        if(seller_serialize.is_valid()):
            seller_serialize.save()
            return JsonResponse(seller_serialize.data,status=status.HTTP_200_OK)
        else:
            return HttpResponse("Error in serialization",status=status.HTTP_400_BAD_REQUEST)
    else:
        return HttpResponse("Get Method Not Allowed",status=status.HTTP_404_NOT_FOUND)
