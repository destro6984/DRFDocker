from django.shortcuts import render
from .models import Idea,Vote
from rest_framework import viewsets
from .seralizers import *


# Create your views here.


class IdeaViewSet(viewsets.ModelViewSet):
    queryset = Idea.objects.all()
    serializer_class = IdeaSeralizer


class VoteViewSet(viewsets.ModelViewSet):
    queryset = Vote.objects.all()
    serializer_class = VoteSeralizer
