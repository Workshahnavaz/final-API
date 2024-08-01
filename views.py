from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from.models import *
from.serializers import *

@api_view(['GET'])
def Chat(request):
    done = parentstudent.objects.all()
    serializer = perantstudentserializers(done,many = True)
    return Response({"status" : 200, "Loading" : serializer.data,"show" : "compleated"})

@api_view(['POST'])
def info(request):
    data = request.data
    serializer = perantstudentserializers(data=request.data)
    if not serializer.is_valid():
        return Response({"status" : 201, "show" : "incomplete"})
    serializer.save()
    return Response({"status" : 200, "loading" : data, "show" : "compleated"})

@api_view(['PUT'])
def details(request,id):
    try:
        goes = parentstudent.objects.get(id=id)
        serializer = perantstudentserializers(goes,data=request.data)
        if not serializer.is_valid():
            return Response({"status" : 201, "show" : "incomplete"})
        serializer.save()
        return Response({"status" : 200, "loading" : serializer.data, "show" : "compleated"})
    except Exception as T:
        return Response({'status' : 400, "show" : "error"})
    

@api_view(['PATCH'])
def database(request,id):
    try:
        goes = parentstudent.objects.get(id=id)
        serializer = perantstudentserializers(goes,data=request.data,partial=True)
        if not serializer.is_valid():
            return Response({"status" : 201, "show" : "incomplete"})
        serializer.save()
        return Response({"status" : 200, "loading" : serializer.data, "show" : "compleated"})
    except Exception as T:
        return Response({'status' : 400, "show" : "error"})

@api_view(['DELETE'])
def metter(request,id):
    try:
        goes = parentstudent.objects.get(id=id)
        goes.delete()
        return Response({"status" : 200,  "show" : "delete"})
    except Exception as T:
        return Response({'status' : 400, "show" : "error"})
