from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

class myAuthenticationForm(AuthenticationForm):
    class Meta:
        model=User
        fields= ['username', 'password']

    def __init__(self, *args, **kwargs):
        super(myAuthenticationForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control my-1'
        self.fields['password'].widget.attrs['class'] = 'form-control my-2'

class myUserCreationForm(UserCreationForm):
    class Meta:
        model=User
        fields= ['username', 'password1','password2', 'first_name','last_name']

    def __init__(self, *args, **kwargs):
        super(myUserCreationForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control my-1'
        self.fields['password1'].widget.attrs['class'] = 'form-control my-1'
        self.fields['password2'].widget.attrs['class'] = 'form-control my-1'
        self.fields['first_name'].widget.attrs['class'] = 'form-control my-1'
        self.fields['last_name'].widget.attrs['class'] = 'form-control my-1'