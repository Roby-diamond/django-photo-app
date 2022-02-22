from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView
import uuid
import boto3
from .models import Photo


S3_BASE_URL = 'https://s3.us-east-1.amazonaws.com/'
BUCKET = 'photodeck'
# Create your views here.

def home(request):
    return render(request, 'home.html')

def upload_photo(request):
    photo_file = request.FILES.get('photo-file', None)
    if photo_file:
        s3 = boto3.client('s3')
        key = uuid.uuid4().hex[:6] + photo_file.name[photo_file.name.rfind('.'):]
        try:
            s3.upload_fileobj(photo_file, BUCKET, key)
            url = f"{S3_BASE_URL}{BUCKET}/{key}"
            photo = Photo(url=url)
            photo.save()
        except:
            print('An error occured uploading file to S3')
    return redirect('home')

class PhotoCreate(CreateView):
    model = Photo
    fields = ('url',)