from typing import Any
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

#burada metaya müdahale edeceğimizi nerden biliyoruz? veya fieldsdaki alanların nereden geldiğini? User ve UserCreationForm a bakınca bir şey anlayamadım
class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2']


    #ANLAMADIM..
    
    def __init__(self, *args, **kwargs):
        super(UserForm,self).__init__(*args, **kwargs)
        # self.fields['username'].widget.attrs.update({'class':'form-control'})
        # self.fields.help_text = "<b> Kullanıcı adının gerilmesi zorunludur </b>"
        for name,field in self.fields.items():
            field.widget.attrs.update({'class':'form-control mb-2'})
