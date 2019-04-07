from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Post
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
import datetime
# Create your views here.
def index(request):
	return render(request,"index.html")

def login_user(request):
	if request.method=="POST":
		form=AuthenticationForm(request,request.POST)
		if form.is_valid():
			username=form.cleaned_data.get('username')
			password=form.cleaned_data.get('password')
			user=authenticate(username=username,password=password)
			if user is not None:
				login(request,user)
				request.session['username']=username
				return redirect('main:dashboard')
		else:
			for msg in form.error_messages:
				print(form.error_messages[msg])

	form=AuthenticationForm()
	return render(request,"login.html",{"form":form})

def signup(request):
	if request.method=="POST":
		form=UserCreationForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('main:login_user')
		else:
			for msg in form.error_messages:
				print(form.error_messages[msg])
	form=UserCreationForm()
	return render(request,"signup.html",{"form":form})

def dashboard(request):
	if request.method=="POST":

		if 'post' in request.POST:
			created_by=request.session['username']
			created_on=datetime.date.today()
			created_at=datetime.time()
			likes=0
			dislikes=0
			content=request.POST.get("content")
			t=Post.objects.get_or_create(content=content,created_by=created_by,created_on=created_on,created_at=created_at,likes=likes,dislikes=dislikes)
			t[0].save()
			return redirect("main:dashboard")

		elif 'like' in request.POST:
			buttonvalue=request.POST.get("like")
			t=Post.objects.get(post_id=buttonvalue)
			current_likes=t.likes
			updated_likes=current_likes+1
			t.likes=updated_likes
			t.save()

		elif 'dislike' in request.POST:
			buttonvalue=request.POST.get("dislike")
			t=Post.objects.get(post_id=buttonvalue)
			current_dislikes=t.dislikes
			updated_dislikes=current_dislikes+1
			t.dislikes=updated_dislikes
			t.save()

	data=Post.objects.all()
	print(request.session['username'])
	return render(request,"dashboard.html",context={"data":data,"username":request.session['username']})


def logout_user(request):
	logout(request)
	request.session.flush()
	return redirect('main:index')