from django.urls import path
from . import views

app_name = 'restaurant'

urlpatterns = [
    path('menu/',views.MenuItemView.as_view(), name='menu-list-create'),
    path('menu<int:pk>/',views.SingleMenuItemView.as_view(), name='menu-retrieve-update-delete'),
]
