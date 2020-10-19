from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response
from .serializers import NoteSerializer, CategorySerializer
from django.shortcuts import render,redirect
import logging

from .models import Notes, Category

logger = logging.getLogger(__name__)


class noteclass(generics.CreateAPIView):

    queryset = Notes.objects.all()
    serializer_class = NoteSerializer

    def create(self, request, *args, **kwargs):

        super(noteclass, self).create(request, args, kwargs)

        response = {"status_code": status.HTTP_200_OK,
                    "message": "Successfully created",
                    "result": request.data}

        return Response(response)

    def homepage(request):

        data = Notes.objects.all()

        context = {'data': data}

        logger.info(data)

        return render(request, 'home.html', context)

class notepost(generics.ListAPIView):

    queryset = Notes.objects.all()

    serializer_class = NoteSerializer

    def retrieve(self, request, *args, **kwargs):

        super(notepost, self).retrieve(request, args, kwargs)

        instance = self.get_object()

        serializer = self.get_serializer(instance)

        data = serializer.data

        logger.info(data)

        response = {"status_code": status.HTTP_200_OK,
                    "message": "Successfully retrieved",
                    "result": data}

        return Response(response)


    def indexpage(request):

        data = Notes.objects.all()

        context = {'data': data}

        logger.info(data)

        return render(request, 'display_note.html', context)



    # def post(self, request):
    #
    #     title = request.POST["description"]
    #
    #     date = str(request.POST["date"])
    #
    #     category = request.POST["category_select"]
    #
    #     #            tag = request.POST["tag"]
    #
    #     content = title + " -- " + date + " " + category
    #
    #     Todo = Notes(title=title, content=content, due_date=date, category=Category.objects.get(name=category))
    #
    #     Todo.save()
    #
    #     return Response(status=status.HTTP_200_OK)