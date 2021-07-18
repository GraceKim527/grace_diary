from django.shortcuts import get_object_or_404, render, redirect
from django.utils import timezone
from .models import Blog, Hashtag
from .forms import CreateForm, CommentForm, HashtagForm
from django.http import request

# Create your views here.

def main(request):
    blogs = Blog.objects.all()
    c_form = CommentForm()
    hashtags = Hashtag.objects
    return render(request, 'main.html', {'blogs':blogs, 'c_form':c_form, 'hashtags':hashtags})

def write(request):
    return render(request, 'write.html')

def comment(request, id):
    blog = get_object_or_404(Blog,id=id)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post_id = blog
            comment.text = form.cleaned_data['text']
            comment.save()
            return redirect('main') # 여기 id지움
    else:
        form=CommentForm()
        return render(request, 'main.html', {'blog':blog, 'form':form})     

def create(request, blog=None):
    if request.method == 'POST':
        form = CreateForm(request.POST, request.FILES)
        if form.is_valid():
            blog = form.save(commit = False)
            blog.pub_date = timezone.now()
            blog.save()
            form.save_m2m()
            return redirect('main')
    else:
        form = CreateForm(instance=blog)
        return render(request, 'write.html', {'form':form})
    # blog = Blog()
    # blog.title = request.POST['title']
    # blog.content = request.POST['content']
    # blog.pub_date = timezone.now()
    # blog.writer = request.POST['writer']   
    # blog.save()
    # return redirect('main')



def edit(request, id):
    edit_blog = Blog.objects.get(id=id)
    return render(request, 'edit.html', {'blog': edit_blog})

def update(request, id):
    post = get_object_or_404(Blog, id=id)
    blog = CreateForm()
    if request.method == 'POST':
        blog = CreateForm(request.POST, instance = post)
        if blog.is_valid():
            blog = blog.save(commit = False)
            blog.pub_date = timezone.now()
            blog.save()
            return redirect('main')
    else:
        blog = CreateForm(instance = post)
        return render(request, 'main.html', {'blog':blog})


    # update_blog = Blog.objects.get(id=id)
    # update_blog.title = request.POST['title']
    # update_blog.writer = request.POST['writer']
    # update_blog.content = request.POST['content']
    # update_blog.pub_date = timezone.now()
    # update_blog.save()
    # return redirect('main')

def delete(request, id):
    delete_blog = Blog.objects.get(id=id)
    delete_blog.delete()
    return redirect('main')

def hashtagform(request, hashtag=None):
    if request.method == 'POST':
        form = HashtagForm(request.POST, instance=hashtag)
        if form.is_valid():
            hashtag = form.save(commit=False)
            if Hashtag.objects.filter(name=form.cleaned_data['name']):
                form = HashtagForm()
                error_message = "이미 존재하는 해시태그 입니다."
                return render(request, 'hashtag.html', {'form':form, "error_message":error_message})
            else:
                hashtag.name = form.cleaned_data['name']
                hashtag.save()
            return redirect('main')
    else:
        form = HashtagForm(instance=hashtag)
        return render(request, 'hashtag.html', {'form':form})

def search(request, hashtag_id):
    hashtag=get_object_or_404(Hashtag, pk=hashtag_id)
    return render(request, 'search.html', {'hashtag':hashtag})