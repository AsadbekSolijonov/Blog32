from django.contrib import messages
from django.core.mail import send_mail
from django.http import HttpResponse
from django.shortcuts import render, redirect

from account.forms import CustomUserCreationForm, CustomUserChangeForm, ProfileChangeForm
from account.models import Profile


def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            Profile.objects.create(user=user)
            messages.success(request, f"{user.username} muvoffaqqiyatli yaratildi!")
            return redirect('login')
    else:
        form = CustomUserCreationForm()

    context = {
        "form": form
    }
    return render(request, 'account/register.html', context=context)


def profile(request):
    return render(request, 'account/profile.html')


def change_profile(request):
    if request.method == 'POST':
        user_form = CustomUserChangeForm(request.POST, instance=request.user)
        profile_form = ProfileChangeForm(request.POST, request.FILES, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            profile_form.save()
            messages.warning(request, f"{user.username} muvoffaqqiyatli o'zgartirildi!")
        return redirect('profile')
    else:
        user_form = CustomUserChangeForm(instance=request.user)
        if not hasattr(request.user, 'profile'):
            Profile.objects.create(user=request.user)
        profile_form = ProfileChangeForm(instance=request.user.profile)
    context = {
        'u_form': user_form,
        'p_form': profile_form
    }
    return render(request, 'account/change_profile.html', context=context)


def test_send_mail(request):
    subject = request.POST.get('subject')
    message = request.POST.get('message')
    to_email = request.POST.get('email')
    if request.method == 'POST':
        send_mail(
            subject,
            message,
            'iamsolijonovasadbek@gmail.com',
            [to_email],
            fail_silently=True
        )
        return render(request, 'mail/send_mail_success.html')

    else:
        return render(request, 'mail/send_mail.html')
