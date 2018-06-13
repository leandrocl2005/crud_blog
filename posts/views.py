from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from .models import Post
from .forms import PostForm
from django.contrib.auth.decorators import login_required

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request,'home/index.html',{'posts': posts})

@login_required
def post_create(request):
  if request.method == "POST":
    form = PostForm(request.POST or None, request.FILES or None)
    if form.is_valid():
      post = form.save(commit=False)
      post.published_date=timezone.now()
      post.save()
      return redirect('post_list')
  else:
    form = PostForm()
  return render(request,'posts_templates/posts_new.html',{'form': form})

def post_delete_list(request):
  posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
  return render(request,'posts_templates/posts_delete_list.html',{'posts': posts})

@login_required		
def post_delete(request, id):
  post = get_object_or_404(Post, pk=id)
  form = PostForm(request.POST or None,request.FILES or None,instance=post)
  if request.method == 'POST':
    post.delete()
    return redirect('post_list')
  return render(request,'posts_templates/posts_delete_confirm.html',{'form':form, 'post':post.title})

def post_edit_list(request):
  posts = Post.objects.filter(
    published_date__lte=timezone.now()
  ).order_by('published_date')
  return render(request,
    'posts_templates/posts_edit_list.html',
    {'posts': posts})

@login_required
def post_edit(request, id):
  post = get_object_or_404(Post, pk=id)
  if request.method == "POST":
    form = PostForm(request.POST,
      instance=post)
    if form.is_valid():
      post = form.save(commit=False)
      post.published_date=timezone.now()
      post.save()
      return redirect('post_list')
  else:
    form = PostForm(instance=post)
  return render(request,
    'posts_templates/posts_edit.html',
    {'form': form})