from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import loader
from django.views import generic
from .models import Post

def home(request):
  return render(request,"index.html")

def results(req,usn):
  return HttpResponse("%s"%usn)

def marks(req,marks):
  if(marks<40):
    res="Fail"
  else:
    res="Pass"
  return HttpResponse("Your result is <b>%s</b>"%res)

def login(request):
  res=None
  users={"admin":"root"}
  if request.method=='POST':
    username=request.POST.get('username')
    password=request.POST.get('password')
    if username in users:
      if users[username]==password:
        res="<h1>Login successfull! Welcome "+username+"</h1>"
      else:
        res="<div class='error'>Invalid password</div>"
    else:
      res="<div class='error'>User not found</div>"
  else:
    res="<div class='error'>Invalid request</div>"
  temp=loader.get_template("home.html")
  return HttpResponse(temp.render({"result":res}))


class PostList(generic.ListView):
  queryset=Post.objects.filter(status=1).order_by('-created_on')
  template_name='posts.html'

class PostDetail(generic.DetailView):
  model=Post
  template_name='post2.html'