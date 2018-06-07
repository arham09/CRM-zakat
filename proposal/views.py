from django.shortcuts import render, redirect
from .forms import DocumentForm

# Create your views here.
def model_form_upload(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/index')
    else:
        form = DocumentForm()
    return render(request, 'proposal/model_form_upload.html', {
        'form': form
    })