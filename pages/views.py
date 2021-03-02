from django.shortcuts import render
from .models import Page
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required(login_url="login")
def page(request, request_slug):
    page = Page.objects.get(slug=request_slug)
    return render(request, 'pages/page.html', {
        'page': page
    })
