from django import forms
from .models import Profile
from django.contrib.auth.hashers import check_password


def min_length(value):
    if len(value) < 2:
        raise forms.ValidationError('2글자 이상 입력해주세요')

class LoginForm(forms.Form):
    username = forms.CharField(
        label='아이디',
        max_length=10, 
        validators=[min_length],
        widget=forms.TextInput(
            attrs={
                'class':'form-group',
                'place_holder':'아이디',
                'required': 'True',
                }
        ),
        error_messages = {
            'required': '아이디를 입력해주세요'
        }
    )

    password = forms.CharField(
        label='비밀번호',
        widget=forms.PasswordInput(
            attrs={
                'class':'form-group',
                'place_holder':'비밀번호',
                'required':'True',
                }
        ),
        error_messages = {
            'required': '비밀번호를 입력해주세요'
        }
    )

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get('username')
        password = cleaned_data.get('password')

        if username and password:
            try:
                user = Users.objects.get(username=username)
                if not check_password(password, user.password):
                    self.add_error('password','비밀번호를 틀렸습니다.')
                else:
                    self.user_id = user.id
            except Exception:
                    self.add_error('username', '존재하지 않는 아이디 입니다.')
    
