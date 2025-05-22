from django.shortcuts import render
from rest_framework import viewsets
from .models import Meal , Rating
from . serializers import MealSerializer, RatingSerializer


# Create your views here.


class MealViewSet(viewsets.ModelViewSet):
    queryset = Meal.objects.all()
    serializer_class = MealSerializer
    # permission_classes = [IsAuthenticated]
    # authentication_classes = [TokenAuthentication]
    # filter_backends = [DjangoFilterBackend]
    # filterset_fields = ['title', 'description']
    
    
class RatingViewSet(viewsets.ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer
    # permission_classes = [IsAuthenticated]
    # authentication_classes = [TokenAuthentication]
    # filter_backends = [DjangoFilterBackend]
    # filterset_fields = ['meal', 'user', 'stars']