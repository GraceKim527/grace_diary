from django.shortcuts import get_object_or_404, render
from django.shortcuts import redirect
from django.utils import timezone
from .models import Blog
from .forms import CreateForm

# Create your views here.

def main(request):
    blogs = Blog.objects.all()
    return render(request, 'main.html', {'blogs':blogs})

def write(request):
    return render(request, 'write.html')

def create(request):
    if request.method == 'POST':
        blog = CreateForm(request.POST)
        if blog.is_valid():
            blog = blog.save(commit = False)
            blog.pub_date = timezone.now()
            blog.save()
            return redirect('main')
    else:
        blog = CreateForm
        return render(request, 'main.html', {'blog':blog})
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