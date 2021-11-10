from django.shortcuts import render, redirect
from django.views.generic import FormView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from ..forms import ProfileForm
from ..models import UserProfileModel


class ProfileView(LoginRequiredMixin, FormView):
    template_name = 'profile.html'
    login_url = reverse_lazy('login')

    def get(self, request, userid):
        self_flag = 0
        sudo_flag = 0
        if self.request.user.id == userid:
            profiles = UserProfileModel.objects.get_or_create(username=self.request.user)
            profile = profiles[0]
        else:
            profiles = UserProfileModel.objects.all().filter(username=userid)
            if not profiles:
                profile = {
                    'username': 'No user for user ID :' + str(userid) + ' available.'
                }
            else:
                profile = profiles[0]
        if self.request.user.id == userid:
            self_flag = 1
        if request.user.is_superuser:
            print('aaa')
            sudo_flag = 1
        return render(request, self.template_name, {
            'profile': profile,
            'if_self': self_flag,
            'if_sudo': sudo_flag
        })


class ProfileModifyView(LoginRequiredMixin, FormView):
    template_name = 'profile_modify.html'
    form_class = ProfileForm
    login_url = reverse_lazy('login')

    def get(self, request):
        profile, create = UserProfileModel.objects.get_or_create(username=self.request.user)
        profile_form = self.form_class(instance=profile)
        return render(request, self.template_name, {'form': profile_form,})

    def post(self, request):
        profiles = UserProfileModel.objects.all().filter(username=self.request.user)
        form = self.form_class(request.POST, request.FILES, instance=profiles[0])
        if form.is_valid():
            form.save()
        return redirect('profile', self.request.user.id)

