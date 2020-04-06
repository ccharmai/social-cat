from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from .models import Comments, Likes
from crud.models import Cats
from django.http import JsonResponse
from django.contrib.auth.models import User


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


@login_required
@require_POST
def LikeAjaxView(request):
	user_id = request.POST['user_id']
	cat_id = request.POST['cat_id']
	user = get_object_or_404(User, id=user_id)

	cat = get_object_or_404(Cats, id=cat_id)
	cats_likes = Likes.objects.filter(cat=cat)
	if cats_likes.filter(user=user).count():
		cats_likes.filter(user=user).delete()
		return JsonResponse({'status': 'unliked'})
	else:
		like = Likes(user=user, cat=cat)
		like.save()
		return JsonResponse({'status': 'liked'})

def GetLikeCount(request):
	cat_id = request.GET['cat_id']
	cat = get_object_or_404(Cats, id=cat_id)
	cats_likes = Likes.objects.filter(cat=cat)
	count = cats_likes.count()
	answer = {}
	answer['count'] = count
	return JsonResponse(answer)

def LogRedirect(request):
	return redirect('login')
