from django.db import models
from stdimage import StdImageField

class Album(models.Model):
    name = models.CharField('Nome', max_length=50)
    description = models.TextField('Descrição', max_length=200, default=" ")
    image = StdImageField('Imagem', upload_to='album_images/', blank=False,
                          variations={
                              'thumbnail': {"width": 225, "height": 225, "crop": True}
                          })
    artist = models.ForeignKey('Artist', on_delete=models.CASCADE, related_name="album", default='')
    created = models.DateTimeField('Criação', auto_now_add=True)

    class Meta:
        ordering = ["-created"]

    def __str__(self):
        return self.name

class Artist(models.Model):
    name = models.CharField('Nome', max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Artista'
        verbose_name_plural = 'Artistas'