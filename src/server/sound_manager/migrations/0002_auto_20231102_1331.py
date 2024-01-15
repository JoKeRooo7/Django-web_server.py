# Generated by Django 3.2.22 on 2023-11-02 13:31

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('sound_manager', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='soundfile',
            name='title',
        ),
        migrations.AddField(
            model_name='soundfile',
            name='uploaded_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='soundfile',
            name='file',
            field=models.FileField(upload_to='audio_files/'),
        ),
    ]