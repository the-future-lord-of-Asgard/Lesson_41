from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Advertisements81
from .forms import Advertisement81Form
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required


def index(request):
    advertisements = Advertisements81.objects.all()
    context = {'advertisements': advertisements}
    return render(request, 'index.html', context)

def top_sellers(request):
    return render(request, 'top-sellers.html')

@login_required(login_url=reverse_lazy('login'))
def advertisement_post(request):
    if request.method == "POST":
        form = Advertisement81Form(request.POST, request.FILES)
        if form.is_valid():
            new_advertisement = form.save(commit=False)
            new_advertisement.user = request.user
            new_advertisement.save()
            url = reverse('main-page')
            return redirect(url)
    else:
        form = Advertisement81Form()
    context = {'form': form}
    return render(request, 'advertisement-post.html', context)