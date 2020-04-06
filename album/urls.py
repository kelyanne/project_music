from django.urls import path
from album import views

urlpatterns = [
    path('', views.IndexTemplateView.as_view(), name='index'),
    path('album/list', views.AlbumList.as_view(), name='album_list'),
    path('album/add', views.AlbumCreate.as_view(), name='album_new'),
    path('album/edit/<slug:pk>', views.AlbumUpdate.as_view(), name='album_edit'),
    path('album/delete/<slug:pk>', views.AlbumDelete.as_view(), name='album_delete'),
    path('artist/add', views.ArtistCreate.as_view(), name='artist_new'),
    path('artist/list', views.ArtistList.as_view(), name='artist_list'),
    path('artist/edit/<slug:pk>', views.ArtistUpdate.as_view(), name='artist_edit'),
    path('artist/delete/<slug:pk>', views.ArtistDelete.as_view(), name='artist_delete'),
    path('artist/detail/<slug:pk>', views.ArtistDetail.as_view(), name='artist_detail'),
]