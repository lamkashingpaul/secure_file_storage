from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Document
from .forms import DocumentForm
import os


@login_required(login_url='/members/login_user/')
def remove_file(request, file_id):
    file_query = Document.objects.filter(id=file_id)

    if file_query:
        file = file_query.first()

        if request.user == file.user:

            if os.path.exists(file.file.path):
                os.remove(file.file.path)
                os.removedirs(os.path.dirname(file.file.path))
                file.delete()

            messages.success(request, 'File deleted successfully')
        else:
            messages.success(request, 'You are not authorized to delete this file')

    return redirect('list_files')


@login_required(login_url='/members/login_user/')
def upload_file(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.user = request.user
            obj.save()
            messages.success(request, 'File uploaded successfully')
            return redirect('upload_file')
    else:
        form = DocumentForm()

    return render(request, 'files/upload.html', {'form': form})


@login_required(login_url='/members/login_user/')
def all_files(request):
    file_list = Document.objects.filter(user=request.user)
    return render(request, 'files/file_list.html', {'file_list': file_list})


def home(request):
    return render(request, 'files/home.html')
