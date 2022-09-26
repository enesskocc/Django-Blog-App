from django.shortcuts import render, get_object_or_404, redirect
from blog.models import Post, Comment, Like
from .forms import FormPost, FormComment
from django.contrib.auth.decorators import login_required
from django.contrib import messages


def post_list(request):
    form_posts = Post.objects.all().order_by('-publish_date')
    context = {
        "form_posts" : form_posts,
    }

    return render(request, "blog/post_list.html", context)

@login_required
def post_create(request):
    form_post = FormPost(request.POST or None, request.FILES)
    if form_post.is_valid():
        formmm = form_post.save(commit=False)
        formmm.user = request.user
        formmm.save()
        messages.success(request,"Successfully Created")
        return redirect('list') 

    context = {
        'form_post': form_post
    }

    return render(request, 'blog/post_create.html', context)

@login_required
def post_delete(request, pk):
    form_post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form_post.delete()
        messages.success(request,"Successfully Deleted")
        return redirect('list') ##! burayi sonra degistir!

    context = {
        'form_post' : form_post
    }

    return render(request, 'blog/post_delete.html', context)

@login_required(login_url='user_login') ## böyde yapilabilir asagidakinen farkli olarak!
def post_update(request, pk):
    form_post = get_object_or_404(Post, pk=pk)
    form2 = FormPost(instance=form_post)
    if request.method == "POST":
        form2 = FormPost(request.POST, instance=form_post)
        if form2.is_valid():
            form2.save()
            messages.success(request,"Successfully Updated")
            return redirect('list') 

    context = {
        'form2': form2
    }

    return render(request, 'blog/post_update.html', context)

@login_required ## sadece login olan görebiliyor! settingsede LOGIN_URL = 'user_login' yaz!
def post_details(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post_comment = Comment.objects.filter(post=post.id)
    form_comment = FormComment(request.POST or None)
    if form_comment.is_valid():

        comment = form_comment.save(commit=False)
        comment.post = post
        comment.user = request.user
        comment.save()
        return redirect('detail', pk)
    print(post_comment)

    context = {
        'post': post,
        'form_comment': form_comment,
        'post_comment': post_comment
    }

    return render(request, 'blog/detail.html', context)


def post_like(request,id):
     if request.user.is_authenticated:
        blog = Post.objects.get(id=id)
        like_qs = Like.objects.filter(user=request.user,post=blog)
        if like_qs:
            like_qs[0].delete()
        else:
            Like.objects.create(user =request.user,post=blog)
     return redirect("list")