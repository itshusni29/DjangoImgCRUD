from django.shortcuts import render, redirect
from .models import Profiles
from .forms import ProfileForm

# Create your views here.

def profile_list(request):
    profiles = Profiles.objects.all()
    mydict = {'profiles': profiles}
    return render(request, 'list.html', context=mydict)

def profile_upload(request):
    mydict = {}
    form = ProfileForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('profile_list')
    
    mydict['form'] = form
    return render(request, 'upload.html', mydict)

def edit_profile(request, id):
    one_rec = Profiles.objects.get(id=id)
    form = ProfileForm(request.POST or None, request.FILES or None, instance=one_rec)
    if form.is_valid():
        form.save()
        return redirect('profile_list')
    mydict = {'form': form}
    return render(request, 'edit.html', context=mydict)

def delete_form(request, id):
    profile = Profiles.objects.get(id=id)
    if request.method == 'POST':
        profile.delete()
        return redirect('profile_list')
    return render(request, 'delete.html', {'profile': profile})


def view_profile(request, id):
    mydict = {}
    one_rec = Profiles.objects.get(id=id)
    mydict['profile'] = one_rec
    return render(request, 'view.html', mydict)