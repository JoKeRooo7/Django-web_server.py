from django.shortcuts import render, redirect
from .forms import SoundFileForm
from django.contrib import messages
from django import forms
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST, require_GET
from django.http import JsonResponse

import os

MEDIA_PATH = "media/audio_files/"

if not os.path.exists(MEDIA_PATH):
    os.makedirs(MEDIA_PATH)


def find_music():
    music_files = []

    for root, dirs, files in os.walk(MEDIA_PATH):
        for file in files:
            # if file.lower().endswith(('.mp3', '.ogg', '.wav')):
            music_files.append(file)
    return music_files


@require_GET
def music_list(request):
    music_files = find_music()
    return JsonResponse({'music_files': music_files})


def home(request):
    return render(request, "home.html", {"music_files": find_music()})


def save_files(uploaded_file):
    with open(
        os.path.join(
            MEDIA_PATH, uploaded_file.name), "wb") as destination:
        for chunk in uploaded_file.chunks():
            destination.write(chunk)


@csrf_exempt
@require_POST
def upload_files(request):
    if request.method == "POST":
        form = SoundFileForm(request.POST, request.FILES)
        if form.is_valid():
            uploaded_file = form.get_audio_files()
            if isinstance(uploaded_file, forms.ValidationError):
                error = str(uploaded_file)
                messages.error(request, error)
            else:
                file_name = str(uploaded_file)
                if file_name in find_music():
                    messages.error(request, "Файл уже существует")
                else:
                    save_files(uploaded_file)
        else:
            error = form.errors.get("audio_file")
            messages.error(request, error)

    else:
        form = SoundFileForm()

    return redirect("home")
