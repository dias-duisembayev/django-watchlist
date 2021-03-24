from django.urls import reverse_lazy
from django.views.generic import ListView, UpdateView, CreateView, DeleteView

from .models import Watch, UserCreateForm


class WatchListView(ListView):
    model = Watch
    template_name = 'home.html'

    def get_queryset(self):
        user = self.request.user
        if user.is_authenticated:
            return Watch.objects.filter(author=user).filter(finished=False)


class WatchListFinishedView(ListView):
    model = Watch
    template_name = 'home.html'

    def get_queryset(self):
        user = self.request.user
        if user.is_authenticated:
            return Watch.objects.filter(author=user).filter(finished=True)


class WatchUpdateView(UpdateView):
    model = Watch
    template_name = 'watch.html'
    fields = ['name', 'description', 'link', 'finished']
    success_url = reverse_lazy('home')

    def get_queryset(self):
        return Watch.objects.filter(author=self.request.user, id=self.kwargs.get('pk'))


class WatchCreateView(CreateView):
    model = Watch
    template_name = 'watch_new.html'
    fields = ['name', 'description', 'link', 'finished']
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class WatchDeleteView(DeleteView):
    model = Watch
    success_url = reverse_lazy('home')

    def get_queryset(self):
        return Watch.objects.filter(author=self.request.user, id=self.kwargs.get('pk'))


class SignUpView(CreateView):
    form_class = UserCreateForm
    success_url = reverse_lazy('home')
    template_name = 'signup.html'
