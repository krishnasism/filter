from django.shortcuts import render
from django.http import HttpResponse
import app.classes.filter as filters
# Create your views here.
from django.core.files.storage import FileSystemStorage
import os

def imageUpload(request):
    if request.method == 'POST' and request.FILES['myfile']:
        BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(BASE_DIR+'\\app\\static\\images\\'+myfile.name, myfile)
        #uploaded_file_url = fs.url(filename)
        
        filename=filters.applyFilter(filename)
        link=True
        return render(request,'home.html',{"filename":filename,"link":link})
        #text = "Image Uploaded<br><br>"+imageSumm1
        #return HttpResponse(text)
    
def homePageView(request):
    link=False
    return render(request,'home.html',{"link":link})