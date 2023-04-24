from django.shortcuts import render, redirect
from .forms import ProfileForm
from .models import Profile

# Create your views here.

def index(request, id = 0):
    if request.method == "GET":
        if id == 0:
            form = ProfileForm()
        else:
            model = Profile.objects.get(pk = id)
            form = ProfileForm(instance=model)
        return render(request, 'index.html', {'form':form})
    else:
        if id == 0:
            form = ProfileForm(request.POST)
        else:
            model = Profile.objects.get(pk = id)
            form = ProfileForm(request.POST, instance=model)
        if form.is_valid():
            form.save()
        return redirect('list')
    
def list(request):
    model = Profile.objects.all()
    return render(request, 'list.html', {'model':model})

def delete(request, id):
    model = Profile.objects.get(pk = id)
    model.delete()
    return redirect('list')
   
    
    


# def list(request):
#     model = Profile.objects.all()
#     return render(request, 'list.html', {'model':model})

# def edit(request, id):
#     model = Profile.objects.get(pk = id)
#     form = ProfileForm(instance = model)
#     return render(request, 'edit.html', {'form':form})
        

# def delete(request, id):
    
#     model = Profile.objects.get(pk = id)
#     model.delete()
#     return redirect('list')
    
