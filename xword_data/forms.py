""" for login and logout pages perpuses. we will use the Django built-in form of authentication  """
from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User






# implementing auth form
class AuthenticationForm(AuthenticationForm):
    username = forms.CharField(
        max_length=50,
        widget=forms.TextInput({
            'class': 'form-control',
            'placeholder': 'Username'
        })
    )

    password = forms.CharField(
        label="Password",
        # render the field as input  type  to the password
        widget=forms.PasswordInput({
            'class': 'form-control',
            'placeholder': 'Password'
        })
    )


# function to search for idem matching
def valide_unique_user(err, **criteria):
    user_exits = User.objects.filter(**criteria)

    # if variable different to None, meaning we found a user macthing our criterion
    if user_exits:
        raise forms.ValidationError(err)


# signup form
class JoinForm(forms.Form):
    username = forms.CharField(
        max_length=10,
        widget=forms.TextInput({
            'class': 'form-control',
            'placeholder': 'Username'
        }))
    
    password = forms.CharField(
        min_length=6,
        max_length=10,
        widget=forms.PasswordInput({
            'class': 'form-control',
            'placeholder': 'Password'
        })
    )

# getting the username value and call valide_unique_user for filter
def cleaned_username(self):
    username = self.cleaned_data['username']

    # calling our filter function
    valide_unique_user(
        err='* Username already existss', username=username
    )

    return username


def cleaned_password(self):
    password = self.cleaned_data['password']

    return password


""" we can implement this method for password2, email, ... """