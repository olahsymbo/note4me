from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response
from .serializers import NoteSerializer, CategorySerializer
from django.shortcuts import render,redirect

from .models import Notes, Category


class noteclass(generics.CreateAPIView):

    queryset = Notes.objects.all()
    serializer_class = NoteSerializer

    def create(self, request, *args, **kwargs):

        super(noteclass, self).create(request, args, kwargs)

        response = {"status_code": status.HTTP_200_OK,
                    "message": "Successfully created",
                    "result": request.data}

        return Response(response)

class notepost(generics.ListAPIView):

    queryset = Notes.objects.all()

    serializer_class = NoteSerializer

    def retrieve(self, request, *args, **kwargs):

        super(notepost, self).retrieve(request, args, kwargs)

        instance = self.get_object()

        serializer = self.get_serializer(instance)

        data = serializer.data

        response = {"status_code": status.HTTP_200_OK,
                    "message": "Successfully retrieved",
                    "result": data}

        return Response(response)