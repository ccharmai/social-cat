from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import CatAddForm, CatUpdateForm
from .models import Cats
from django.shortcuts import redirect, reverse
from act.forms import AddCommentForm
from act.models import Comments, Likes
from django.contrib.auth.models import User

def HomeView(request):
	cats = Cats.objects.all()
	return render(request, 'crud/home.html', {'cats': cats})

def CatView(request, id):
	cat = get_object_or_404(Cats, id=id)
	likes = Likes.objects.filter(cat=cat)
	total_likes = likes.count()

	if likes.filter(user=request.user).count():
		liked = True
	else:
		liked = False

	if request.user.is_staff:
		comments = Comments.objects.filter(cat=cat)
	else:
		comments = Comments.objects.filter(cat=cat, deleted=False)

	if request.method == 'POST':
		form = AddCommentForm(request.POST)
		if form.is_valid():
			cd = form.cleaned_data
			comment = Comments(cat=cat, commentator=request.user, body=cd['body'])
			comment.save()
			return redirect(cat.get_absolute_url())
	else:
		form = AddCommentForm()
	return render(request, 'crud/cat.html', {'cat': cat, 'comments': comments, 'form': form, 'likes': likes, 'total_likes': total_likes, 'liked': liked})

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

@login_required
def AdminView(request):
	if not request.user.is_staff:
		return reverse('crud:home')
	users = User.objects.all()
	cats = Cats.objects.all()
	comments = Comments.objects.filter(deleted=True)
	return render(request, 'crud/admin.html', {'users': users, 'cats': cats, 'comments': comments})
