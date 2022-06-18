


from django.forms import ModelForm
from apps.home.models import Etablisment


class EtablismentForm  (ModelForm):
      class Meta:
          model = Etablisment
          fields = '__all__'
