from django.shortcuts import render
from forms.forms import OrderForms
from forms.models import MyForms
# Create your views here.

def add_forms(request):
    template = 'forms/forms.html'
    form = OrderForms()

    if request.method == 'POST':
        form = OrderForms(request.POST or None)

        if form.is_valid():
            MyForms.objects.create(**form.cleaned_data)
            form = OrderForms()

    data = {
        'form':form
    }

    return render(request, template, context=data)


