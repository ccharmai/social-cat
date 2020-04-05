from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib.auth.decorators import login_required
from .models import Comments, Likes
from crud.models import Cats

@login_required
def CommentDeleteView(request, id):
	comment = get_object_or_404(Comments, id=id, commentator=request.user)
	cat = comment.cat
	comment.deleted = True
	comment.save()
	return redirect(cat.get_absolute_url())

@login_required
def LikeView(request, cat_id):
	user = request.user
	cat = get_object_or_404(Cats, id=cat_id)
	cats_likes = Likes.objects.filter(cat=cat)
	if cats_likes.filter(user=user).count():
		cats_likes.filter(user=user).delete()
	else:
		like = Likes(user=user, cat=cat)
		like.save()
	return redirect(cat.get_absolute_url())

def LogRedirect(request):
	return redirect('login')
