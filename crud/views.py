from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import CatAddForm, CatUpdateForm
from .models import Cats
from django.shortcuts import redirect

def HomeView(request):
	cats = Cats.objects.all()
	return render(request, 'crud/home.html', {'cats': cats})

def CatView(request, id):
	cat = get_object_or_404(Cats, id=id)
	return render(request, 'crud/cat.html', {'cat': cat})

@login_required
def AddView(request):
	if request.method == 'POST':
		form = CatAddForm(request.POST)
		if form.is_valid():
			cd = form.cleaned_data
			cat = Cats(owner=request.user, name=cd['name'], sex=cd['sex'], age=cd['age'], breed=cd['breed'], hair=cd['hair'])
			cat.save()
			return render(request, 'crud/added.html', {'name': cd['name'], 'id': cat.id})
	else:
		form = CatAddForm()
	return render(request, 'crud/add.html', {'form': form})

@login_required
def DelView(request, id):
	cat = get_object_or_404(Cats, id=id, owner=request.user)
	name = cat.name
	cat.delete()
	return render(request, 'crud/deleted.html', {'name': name})

@login_required
def UpdateView(request, id):
	cat = get_object_or_404(Cats, id=id, owner=request.user)
	if request.method == 'POST':
		form = CatUpdateForm(instance=cat, data=request.POST)
		if form.is_valid():
			form.save()
			return redirect(cat.get_absolute_url())
	else:
		form = CatUpdateForm(instance=cat)
	return render(request, 'crud/update.html', {'form': form, 'cat': cat})

@login_required
def LKView(request):
	cats = Cats.objects.filter(owner=request.user)
	return render(request, 'crud/lk.html', {'user': request.user, 'cats': cats})

