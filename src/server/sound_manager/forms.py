from django import forms
# from .models import SoundFile для скачивания с бд

AUDIO_FILES = ['mp3', 'ogg', 'wav']


class SoundFileForm(forms.Form):
    audio_file = forms.FileField(required=True)

    def get_audio_files(self):
        uploaded_file = self.cleaned_data.get("audio_file")
        # if not uploaded_file:
        #     return forms.ValidationError("No file uploaded")
        file_extension = uploaded_file.name.split('.')[-1].lower()

        if file_extension not in AUDIO_FILES:
            return forms.ValidationError("Not an audio file(mp3, ogg, wav).")

        return uploaded_file
