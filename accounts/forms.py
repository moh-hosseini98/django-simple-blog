
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ValidationError





class CreateUserForm(UserCreationForm):
    
    class Meta:

        model = User
        fields = ['username','email','password1','password2']


    def clean_email(self):

    
        email = self.cleaned_data['email']

        if User.objects.filter(email=email).exists():



            raise ValidationError('this email already used')

        return email

    def clean_username(self):
        
        username = self.cleaned_data['username']

        if len(username) < 3 :
            raise ValidationError('your username length must greater than 2 char')

        return username     