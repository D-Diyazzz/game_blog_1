from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

from .forms import LoginForm
# Create your views here.


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, username=cd['username'], password=cd['password'])#если что то не правильно вернется NOne
            if user is not None:
                if user.is_active:
                    login(request, user)#сохраняет текущего пользователя в сессии
                    return render(request, 'blog_t/news.html', {'section': 'news'})
                else:
                    return HttpResponse('Disabled account')
            else:
                return HttpResponse('Invalid login')
    else:
        form = LoginForm()#если GET запрос то создаем форму логина
    return render(request, 'lg_au_t/login.html', {'form': form})


@login_required
def news(request):
    return render(request, 'blog_t/news.html', {'section': 'news'})