from django.shortcuts import render
from . import forms


# Create your views here.
# DataFlair #Form #View Functions

def regform(request):
    form = forms.SignUp()
    if request.method == 'POST':
        form = forms.SignUp(request.POST)
        html = 'we have request this form again'
        if form.is_valid():
            html = "The Form is Valid"
    else:
        html = 'welcome for the first time'
    return render(request, 'signup.html', {'html': html, 'form': form})

