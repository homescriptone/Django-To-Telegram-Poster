from django.db import models


class Poster(models.Model):
    link = models.URLField(verbose_name="Lien vers la page", max_length=100000)
    link_name = models.CharField(verbose_name="Nom attribué au lien", default="Site de recherche", max_length=1025, primary_key=True)
    is_posted_on_tg = models.BooleanField(verbose_name="ce lien fut posté", default=False)

    def __str__(self):
        return str(self.is_posted_on_tg)

    def get_link(self):
        return self.link

    def get_link_name(self):
        return self.link_name

    def set_link(self,link, link_name=None):
        self.link = link
        self.link_name = link_name
        self.save()

    def get_post_status(self):
        return self.is_posted_on_tg
