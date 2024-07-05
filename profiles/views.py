from django.shortcuts import render, redirect
from .forms import ProfileForm
from .dynamodb_config import table


def create_profile(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            data = form.cleaned_data
            # Save data to DynamoDB
            table.put_item(
                Item={
                    'name': data['name'],
                    'email': data['email'],
                    'profile_picture': data['profile_picture'].name if data['profile_picture'] else None,
                    'resume': data['resume'].name if data['resume'] else None,
                }
            )
            return redirect('profile_success')
    else:
        form = ProfileForm()

    return render(request, 'profiles/create_profile.html', {'form': form})