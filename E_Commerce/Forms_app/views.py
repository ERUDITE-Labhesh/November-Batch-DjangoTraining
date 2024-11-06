from django.http import JsonResponse
from django.shortcuts import render
from .forms import FileUploadFormClass
from .models import FileUpload

# Create your views here.
def file_upload_form(request):
    if request.method=="POST":
        form=FileUploadFormClass(request.POST,request.FILES)
        if form.is_valid():
            #model form
            form.save()

            #normal form
            # file_upload=FileUpload(name=form.cleaned_data["name"],file=form.cleaned_data["file"])
            # file_upload.save()
            return JsonResponse({
                "success":True
            },status=200)
    if request.method=="GET":
        form=FileUploadFormClass()

    return render(request,"Forms_app/fileupload.html",{"form":form})