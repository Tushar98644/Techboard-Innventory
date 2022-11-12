from django.urls import path
from . import views
urlpatterns = [
    path("", views.home, name='blog-home'),
    path("inventory", views.invent, name='invent-ory'),
    path("inventory/<int:id>/", views.invent, name='update'),
    path("delete/<int:id>",views.delete,name='delete'),
    path("inventory2",views.Inventory_list, name='inventory2'),
    path('book',views.book, name='book'),
    path('book2',views.book_list, name='book2')

    
    # path('result', views.result)
    
]