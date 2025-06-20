from django.contrib.auth import authenticate, login as user_login, logout as user_logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from .forms import ImageParametersForm
from .generation import generate_image
from .models import SystemParameters


# Create your views here.
def index(request):
    return render(request, 'main/index.html')

def gallery_view(request):
    images = []

    for image in SystemParameters.objects.order_by('-created_at'):
        images.append(generate_image(image))
    return render(request, 'main/gallery.html', {'images': images})

@login_required
def my_gallery_view(request, username=None):
    images = SystemParameters.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'main/mygallery.html', {'images': images})

@login_required
def delete_image(request, pk):
    image = get_object_or_404(SystemParameters, id=pk, user=request.user)
    if request.method == 'POST':
        image.delete()
        return redirect('mygallery')
    return redirect('mygallery')

@login_required
def create_view(request):
    img_str = None
    if request.method == 'POST':
        form = ImageParametersForm(request.POST)
        if form.is_valid():
            params = form.save(commit=False)
            params.user = request.user
            action = request.POST.get('action')
            img_str = generate_image(params)
            if action == 'save':
                img_str = generate_image(params)
                params.save()
            elif action == 'render':
                img_str = generate_image(params)
    else:
        form = ImageParametersForm()
    return render(request, 'main/creation.html', {'form': form, 'img_str': img_str})


def login_view(request):
    if request.method == 'POST':
        login = request.POST.get('login')
        password = request.POST.get('password')

        usr = authenticate(request, username=login, password=password)
        if usr is not None:
            user_login(request, usr)
            return HttpResponseRedirect('/')
        else:
            return render(request, 'registration/login.html')
    return render(request, 'registration/login.html')


def register_view(request):
    if request.method == 'POST':
        login = request.POST.get('login')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')

        if password == password2:
            User.objects.create_user(login, password=password)
            usr = authenticate(request, username=login, password=password)
            if usr is not None:
                user_login(request, usr)
                return HttpResponseRedirect('/')
            else:
                return render(request, 'registration/login.html')


    return render(request, 'registration/reg.html')

def logout_user(request):
    user_logout(request)
    return HttpResponseRedirect('/')