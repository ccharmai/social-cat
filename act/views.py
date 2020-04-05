from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Comments

@login_required
def CommentDeleteView(request, id):
	comment = get_object_or_404(Comments, id=id, commentator=request.user)
	cat = comment.cat
	comment.deleted = True
	comment.save()
	return redirect(cat.get_absolute_url())

