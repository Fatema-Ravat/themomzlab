from django.shortcuts import render,redirect
from .forms import PostCreateFrom
from .models import Post
from django.contrib.auth.decorators import login_required

# Create your views here.

def list_post(request):
    posts = Post.objects.all()
    return render(request,'posts/list_post.html',{'posts':posts})

@login_required
def create_post(request):
    if request.method == 'POST':
        post_form = PostCreateFrom(data=request.POST,files=request.FILES)
        if post_form.is_valid():
            new_post = post_form.save(commit=False)
            new_post.user = request.user
            new_post.save()
            return redirect('list_post')
    else:
        post_form = PostCreateFrom()
        return render(request,'posts/create_post.html',{'post_form':post_form})