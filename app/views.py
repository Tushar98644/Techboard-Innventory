from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import InventoryForm
from .models import Inventory
# Create your views here.
def home(request):
    return render(request,'app/index.html')
def invent(request):
    if request.method == "GET":

        form = InventoryForm()

        
        return render(request, 'app/inventory.html',{'form':form})
    else :
        form = InventoryForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/inventory2')
def Inventory_list(request):
    context = {'inventory2':Inventory.objects.all()}
    return render(request,"app/inventory2.html",context)
