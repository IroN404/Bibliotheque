from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _
from . import models

class LivreForms(ModelForm):
    class Meta :
        model = models.Livre
        fields = ('titre','auteur', 'date_parution', 'nombre_pages', 'resume')
        labels = {
            'titre' : _('Titre'),
            'auteur' : _('Auteur'),
            'date_parution' : _('Date de parution'),
            'nombre pages' : _('Nombre de pages'),
            'resume' : _('Résumé'),
        }