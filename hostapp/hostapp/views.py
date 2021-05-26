from django.shortcuts import render
from hostapp.models import audImag

def imagedisplay(request):
    resultsdisplay = audImag.objects.all()
    return render(request, 'index.html', {'audImag':resultsdisplay})
