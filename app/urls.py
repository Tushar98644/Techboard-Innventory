from django.urls import path
from . import views
urlpatterns = [
    path("", views.home, name='blog-home'),
    path("inventory", views.invent, name='invent-ory'),
    path("inventory2",views.Inventory_list, name='inventory2')
    
    # path('result', views.result)
    
]