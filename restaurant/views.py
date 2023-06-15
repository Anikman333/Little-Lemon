from django.shortcuts import render
from .models import Menu
from rest_framework import generics
from .serializers import MenuSerializer
from .models import Booking
from rest_framework import viewsets
from .serializers import BookingSerializer


# Create your views here.
def index(request):
    return render(request, 'index.html', {} )

# API views
class MenuItemView(generics.ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

class SingleMenuItemView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer   

class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer    