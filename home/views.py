from django.shortcuts import render, redirect
from .models import Image
from .forms import ImageForm
# Create your views here.



def image_list(request):
    images = Image.objects.all()
    mydict = {'images': images}
    return render(request, 'image_list.html', context=mydict)

def image_upload(request):
    mydict = {}
    form = ImageForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('/')
    
    mydict['form'] = form
    return render(request, 'image_upload.html', mydict)
    

def edit_image(request, id):
    one_rec = Image.objects.get(id=id)
    form = ImageForm(request.POST or None, request.FILES or None, instance=one_rec)
    if form.is_valid():
        form.save()
        return redirect('/')
    mydict = {'form': form}
    return render(request, 'edit_upload.html', context=mydict)


def delete_image(request, id):
    one_rec = Image.objects.get(id=id)
    if request.method == 'POST':
        one_rec.delete()
        return redirect('/')
    return render(request, 'delete_image.html')

def view_image(request, id):
    mydict = {}
    one_rec = Image.objects.get(id=id)
    mydict['image'] = one_rec
    return render(request, 'view_image.html', mydict)

