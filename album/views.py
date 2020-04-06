from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, TemplateView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from album.models import Album, Artist
from django.db.models import Count


class IndexTemplateView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexTemplateView, self).get_context_data(**kwargs)
        context['artists_top_five'] = (Artist.objects.values('name')
                                           .annotate(count=Count('album'))
                                           .order_by('-count')
                                           .exclude(count=0)[:5])
        context['last_albums'] = Album.objects.all().order_by('-created')[:3]
        context['activate'] = 'home'
        print(context['last_albums'])
        return context


class AlbumList(ListView):
    model = Album
    template_name = 'album_list.html'
    paginate_by = 9
    context_object_name = 'albums'
    paginate_by = 10
    ordering = 'id'

    def get_queryset(self):
        query = self.request.GET.get('search')
        if query:
            albums = Album.objects.filter(name__icontains=query)
        else:
            albums = Album.objects.all()
        return albums


class AlbumCreate(SuccessMessageMixin, CreateView):
    template_name = 'album_form.html'
    model = Album
    fields = '__all__'
    success_url = reverse_lazy('album_new')

    def get_success_message(self, cleaned_data):
        return "Álbum adicionado com sucesso"


class AlbumUpdate(UpdateView):
    template_name = 'album_edit.html'
    model = Album
    fields = '__all__'
    success_url = reverse_lazy('album_list')

    def get_success_message(self, cleaned_data):
        return "Álbum editado com sucesso"


class AlbumDelete(DeleteView):
    model = Album
    template_name = 'album_list.html'
    success_url = reverse_lazy('album_list')


class ArtistCreate(CreateView):
    model = Artist
    fields = '__all__'
    template_name = 'artist_form.html'
    success_url = reverse_lazy('album_new')


class ArtistList(ListView):
    model = Artist
    template_name = 'artist_list.html'
    context_object_name = 'artists'
    paginate_by = 10
    ordering = 'id'


class ArtistDetail(DetailView):
    model = Artist
    template_name = 'artist_detail.html'


class ArtistUpdate(UpdateView):
    template_name = 'artist_edit.html'
    model = Artist
    fields = '__all__'
    success_url = reverse_lazy('artist_list')


class ArtistDelete(DeleteView):
    model = Artist
    template_name = 'artist_list.html'
    success_url = reverse_lazy('artist_list')