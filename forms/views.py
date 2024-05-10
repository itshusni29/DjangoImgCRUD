from django.shortcuts import render, redirect
from profiles.models import Profiles
from .forms import TrainingRequestForm
from .models import TrainingRequest, Attachment
from django.contrib.auth.decorators import login_required

@login_required
def all_training_requests(request):
    training_requests = TrainingRequest.objects.all()
    context = {'training_requests': training_requests}
    return render(request, 'all_training_requests.html', context=context)

@login_required
def create_training_request(request):
    manager_profiles = Profiles.objects.filter(Occupation='mng')
    general_manager_profiles = Profiles.objects.filter(Occupation='gm')
    
    if request.method == 'POST':
        form = TrainingRequestForm(request.POST, request.FILES)
        if form.is_valid():
            training_request = form.save(commit=False)
            training_request.requester = request.user.profile
            training_request.save()

            for attachment in request.FILES.getlist('attachments'):
                attachment_instance = Attachment.objects.create(file=attachment)
                training_request.attachments.add(attachment_instance)

            for attachment in request.FILES.getlist('additional_attachments'):
                attachment_instance = Attachment.objects.create(file=attachment)
                training_request.attachments.add(attachment_instance)

            return redirect('training_request_detail', pk=training_request.pk)
    else:
        form = TrainingRequestForm()

    context = {
        'form': form,
        'manager_profiles': manager_profiles,
        'general_manager_profiles': general_manager_profiles
    }
    return render(request, 'create_training_request.html', context=context)



@login_required
def training_request_detail(request, pk):
    training_request = TrainingRequest.objects.get(pk=pk)
    return render(request, 'training_request_detail.html', {'training_request': training_request})

@login_required
def edit_training_request(request, pk):
    training_request = TrainingRequest.objects.get(pk=pk)
    if request.method == 'POST':
        form = TrainingRequestForm(request.POST, request.FILES, instance=training_request)
        if form.is_valid():
            form.save()
            return redirect('training_request_detail', pk=pk)
    else:
        form = TrainingRequestForm(instance=training_request)
    return render(request, 'edit_training_request.html', {'form': form})

@login_required
def delete_training_request(request, pk):
    training_request = TrainingRequest.objects.get(pk=pk)
    if request.method == 'POST':
        training_request.delete()
        return redirect('home')  # Redirect to home or any other appropriate page
    return render(request, 'delete_training_request.html', {'training_request': training_request})
