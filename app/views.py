from django.http import HttpResponse
from django.shortcuts import redirect, render

from .forms import BookForm, InventoryForm
from .models import Book, Inventory


# Create your views here.
def home(request):
    return render(request,'app/index.html')
def invent(request,id=0):
    if request.method == "GET":
        if id==0:

            form = InventoryForm()
        else:
            inventory = Inventory.objects.get(pk=id)
            form = InventoryForm(instance=inventory)

        
        return render(request, 'app/inventory.html',{'form':form})
    else :
        if id == 0:

            form = InventoryForm(request.POST)
        else:
            inventory = Inventory.objects.get(pk=id)
            form = InventoryForm(request.POST, instance  = inventory)
        if form.is_valid():
            form.save()
        return redirect('/inventory2')
def Inventory_list(request):
    context = {'inventory2':Inventory.objects.all()}
    return render(request,"app/inventory2.html",context)
def delete(request,id):
    inventory = Inventory.objects.all(pk=id)
    inventory.delete()
    return redirect('/inventory2')
def book(request):
    if request.method == "GET":
        form = BookForm()
        return render(request, "app/book.html",{'form':form})
    else:
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/book2')
def book_list(request):
    context = {'book2':Book.objects.all()}
    return render(request,"app/book2.html",context)

