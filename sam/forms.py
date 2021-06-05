from django import forms
from sam.models import Profile
from django.contrib.auth.forms import UserCreationForm


class ProfileModelForm(UserCreationForm):
    password1 = forms.CharField(widget=forms.PasswordInput(
        attrs={"class": "form-control", 'placeholder': 'Password'})
    )
    password2 = forms.CharField(widget=forms.PasswordInput(
        attrs={"class": "form-control", 'placeholder': 'Confirm Password'})
    )

    class Meta:
        model = Profile
        fields = ("first_name", "email",
                  "last_name", "message", "phone", "address", "occupation", "password1", "password2")
        widgets = {
            'first_name': forms.TextInput(attrs={'class': "form-control", "placeholder": "First Name"}),
            'last_name': forms.TextInput(attrs={'class': "form-control", "placeholder": "Last Name"}),
            'email': forms.TextInput(attrs={'class': "form-control", "placeholder": "E-mail Address", "autocomplete": "off"}),
            'phone': forms.TextInput(attrs={'class': "form-control", "placeholder": "Phone number"}),
            'address': forms.TextInput(attrs={'class': "form-control", "placeholder": "Address"}),
            'occupation': forms.TextInput(attrs={'class': "form-control", "placeholder": "Occupation"}),
            'message': forms.Textarea(attrs={'class': "form-control", "rows": "5", "placeholder": "Why do you want to become a member?"}),
        }
    
    def __init__(self, *args, **kwargs):
        super(ProfileModelForm, self).__init__(*args, **kwargs)
        self.fields['email'].widget.attrs.pop("autofocus", None)
