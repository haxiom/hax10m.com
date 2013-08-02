from django.forms import ModelForm
from models import NavigationList

class NavigationListForm(ModelForm):

    class Meta:
        model = NavigationList
