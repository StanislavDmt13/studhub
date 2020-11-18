import os
from django.shortcuts import render
from django.http import FileResponse, JsonResponse
from django.conf import settings
from django.views.decorators.cache import cache_page


# Create your views here.

def base(request):
    return render(request, "base.html")
