from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .models import Prank
from .serializers import PrankSerializer

# Create your views here.
@csrf_exempt
def article_list(request):

    if request.method=='GET':
        prank=Prank.objects.all()
        serializer=PrankSerializer(prank, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method=='POST':
        data=JSONParser().parse(request)
        serializer=PrankSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def article_detail(request, id):
    try:
        prank=Prank.objects.get(id=id)
    except Prank.DoesNotExist:
        return HttpResponse(status=404)
    if request.method=="GET":
        serializer=PrankSerializer(prank)
        return JsonResponse(serializer.data)
    # elif request.method=="POST":
    #     data=JSONParser.parse(request)
    #     serializer=PrankSerializer(data=data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return JsonResponse(serializer.data, status=201)
    #     return JsonResponse(serializer.errors, status=404)

    elif request.method=="PUT":
        data=JSONParser.parse(request)
        serializer=PrankSerializer(prank, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method=="DELETE":
        prank.delete()
        return HttpResponse(status=204)
