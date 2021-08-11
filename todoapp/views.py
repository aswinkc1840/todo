from django.shortcuts import render, redirect

from todoapp.forms import todoforms
from . models import task
# Create your views here.
def index(request):
    obj1 = task.objects.all()
    if request.method=='POST':
        name=request.POST.get('name')
        priority = request.POST.get('priority')
        obj=task(name=name,priority=priority)
        obj.save()

    return render(request,'index.html',{'obj':obj1})


def delete(request,id):
    obj=task.objects.get(id=id)
    if request.method=='POST':
        obj.delete()
        return redirect('/')
    return render(request,'delete.html',{'obj':obj})

def update(request,id):
    obj = task.objects.get(id=id)
    form=todoforms(request.POST or None,instance=obj)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'edit.html',{'obj':obj,'form':form})


