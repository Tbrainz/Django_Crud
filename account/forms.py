from django.forms import ModelForm
from .models import Profile

class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'
        labels = {'fullname': 'Full Name',
                  'mobile':'Phone Number' 
                 }
        
    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)
        self.fields['status'].empty_label = 'select'
        self.fields['fullname'].required = False