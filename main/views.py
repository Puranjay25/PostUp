from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from .models import user,post
import datetime
# Create your views here.
def index(request):
	return render(request,"index.html")

def login_user(request):
	if request.method=="POST":
		username=request.POST.get("username")
		password=request.POST.get("password")
		t=user.objects.filter(username=username)
		if t:
			for t1 in t:
				if password==t1.password:
					#u=authenticate(request,username=username,password=password)
					#if request.user.is_authenticated:
						#login(request,u)
					request.session['username']=username
					#return redirect('main:dashboard',username=username)
					return redirect('main:index')
				else:
					return redirect('main:login_user')
			error="Type correct Password"
			return render(request,"login.html",context={"error":error})
		else:
			error="No user found"
			return render(request,"login.html",context={"error":error})
	return render(request,"login.html")

def signup(request):
	if request.method=="POST":
		firstname=request.POST.get("firstname")
		lastname=request.POST.get("lastname")
		username=request.POST.get("username")
		password=request.POST.get("password")
		confirmpassword=request.POST.get("confirmpassword")


		if password==confirmpassword:
			t=user.objects.get_or_create(firstname=firstname,lastname=lastname,username=username,password=password)
			t[0].save()
		else:
			return redirect('signup',error='Password And Confirm Password do not match')
			error="Password And Confirm Password do not match"
			return render(request,"signup.html",context={"error":error})
	return render(request,"signup.html")

def dashboard(request):
	if request.method=="POST":
		created_by=request.session['username']
		created_on=datetime.date.today()
		created_at=datetime.time()
		likes=0
		dislikes=0
		content=request.POST.get("content")
		t=post.objects.get_or_create(content=content,created_by=created_by,created_on=created_on,created_at=created_at,likes=likes,dislikes=dislikes)
		t[0].save()
		return redirect("main:dashboard")
	data=post.objects.all()
	for d in data:
		print(d.content)
	return render(request,"dashboard.html",context={"data":data})


def logout_user(request):
	logout(request)
	request.session.flush()
	return redirect('main:index')