from django.shortcuts import get_object_or_404, render

# Create your views here.

def forms(request):
    templates = 'forms/forms.html'
    return render(request, templates)