from django.shortcuts import render,get_object_or_404,redirect
from .forms import BlogForm,CommentForm
from .models import Blog,Comment
from django.utils import timezone
# Create your views here.
def home(request):
    blogs=Blog.objects.order_by('-id')
    return render(request,'home.html',{'blogs':blogs})


def post(request):
    if request.method == "POST":
        form=BlogForm(request.POST)
        if form.is_valid():
            blog=form.save(commit=False)
            blog.pub_date=timezone.now()
            blog.save()
            return redirect('home')
    
    else:
        form=BlogForm()
        return render(request,'post.html',{'form':form})


def detail(request,blog_id):
    blog_detail=get_object_or_404(Blog,pk=blog_id)
    if request.method=="POST":
        comment_form=CommentForm(request.POST)
        comment_form.instance.blog_id=blog_id
        if comment_form.is_valid():
            comment=comment_form.save()
    
    comment_form=CommentForm()
    comments=blog_detail.comments.all()
    return render(request,'detail.html',{'blog':blog_detail,'comments':comments,'comment_form':comment_form})


def edit(request,pk):
    blog=get_object_or_404(Blog,pk=pk)
    if request.method == "POST":
        form=BlogForm(request.POST,instance=blog)
        if form.is_valid():
            blog=form.save(commit=False)
            blog.pub_date=timezone.now()
            blog.save()
            return redirect('home')
    
    else:
        form=BlogForm(instance=blog)
        return render(request,'edit.html',{'form':form})

def delete(request,pk):
    blog=Blog.objects.get(id=pk)
    blog.delete()
    return redirect('home')
