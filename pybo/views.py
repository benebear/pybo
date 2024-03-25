from django.shortcuts import render

# Create your views here.

from django.shortcuts import render, redirect
from pybo.forms import PostForm
from pybo.models import Post
from django.core.files.storage import FileSystemStorage

def post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('posts:list')  # 'posts:list'는 게시글 목록을 보여주는 URL의 이름입니다.
    else:
        form = PostForm()
    return render(request, 'posts/post_form.html', {'form': form})


def your_view(request):
    uploaded_image_url = None
    if request.method == 'POST' and 'image' in request.FILES:
        image = request.FILES['image']
        fs = FileSystemStorage()
        filename = fs.save(image.name, image)
        uploaded_image_url = fs.url(filename)

    return render(request, 'answer_form.html', {
        'uploaded_image_url': uploaded_image_url
    })