## likeLion 9th CRUD class_site 'diary'

---

## Result

### modal창 구현

![ezgif com-gif-maker](https://user-images.githubusercontent.com/80322308/119332076-1280af00-bcc3-11eb-8e8e-05b497906913.gif)

### save/edit page
![ezgif com-gif-maker (1)](https://user-images.githubusercontent.com/80322308/119332491-9fc40380-bcc3-11eb-8d50-64e326abce5e.gif)

---

## Of Development

### CRUD

#### create
```html
<form class="form" action = "{% url 'create' %}" method = "POST">
    {% csrf_token %}

    
    <div class="textForm">
        <input type="text" required class="textInput" name="title" id="title">
        <label class="textLabel" for="title">제목</label>
        <span class="spanOverlay"></span>
        <span class="spanBase"></span>
    </div>
    <div class="textForm">
        <input type="text" required class="textInput" name="writer" id="writer">
        <label class="textLabel" for="writer">작성자</label>
        <span class="spanOverlay"></span>
        <span class="spanBase"></span>
    </div>

    <div class="contentForm">
        <textarea name="content" required class="content" id="content" cols="30" rows="10"></textarea>
        <label class="contentLabel" for="content">내용</label>
        <span class="spanOverlay"></span>
        <span class="spanBase"></span>
    </div>


    <button type="submit" class="submitBtn">저장</button>

</form>

```



#### update
id 값을 매개변수로 보내줌
```python
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
```

#### delete
```html
 <a class="btn btn-primary" href="{% url 'delete' blog.id %}" data-bs-dismiss="modal">
<i class="fas fa-times fa-fw"></i>삭제하기</a>
```
```python
def delete(request, id):
    delete_blog = Blog.objects.get(id=id)
    delete_blog.delete()
    return redirect('main')
```

---

