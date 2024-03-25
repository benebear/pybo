from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from common.forms import UserForm
from django.shortcuts import render, redirect
from .forms import PostForm
from .models import Post

def post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('posts:list')  # 'posts:list'는 게시글 목록을 보여주는 URL의 이름입니다.
    else:
        form = PostForm()
    return render(request, 'posts/post_form.html', {'form': form})

def signup(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)  # 사용자 인증
            login(request, user)  # 로그인
            return redirect('index')
    else:
        form = UserForm()
    return render(request, 'common/signup.html', {'form': form})

def my_view(request):
    if request.method == 'POST':
        form = MyForm(request.POST, request.FILES)
        if form.is_valid():
            # form.cleaned_data를 사용하여 폼 데이터를 가져옵니다.
            # 이미지는 request.FILES 안에 있습니다.
            image = form.cleaned_data.get('image')
            # 이미지를 모델과 연결하여 저장합니다.
            # 예: MyModel.objects.create(image=image)
            ...
    else:
        form = MyForm()
    return render(request, 'question_form.html', {'form': form})