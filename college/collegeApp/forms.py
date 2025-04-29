from django import forms
from django.core.exceptions import ValidationError
from .models import *



class UserCreationForm(forms.ModelForm):
    """A form for creating new student users with custom fields and password confirmation."""
    
    password1 = forms.CharField(
        label='Password',
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'id': 'password1',
            'placeholder': 'Enter your password'
        })
    )
    password2 = forms.CharField(
        label='Confirm Password',
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'id': 'password2',
            'placeholder': 'Confirm your password'
        })
    )

    class Meta:
        model = User
        fields = (
            'email',
            'first_name',
            'last_name',
            'enrollment_number',
            'course',
            'branch',
            'year',
            'phone',
            'profile_picture'
        )
        widgets = {
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter your email'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter first name'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter last name'}),
            'enrollment_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter enrollment number'}),
            'course': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter course'}),
            'branch': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter branch'}),
            'year': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter year'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter phone number'}),
            'profile_picture': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }

    def clean_password2(self):
        """Validate that both passwords match."""
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        """Save the student with hashed password."""
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user    

class UserUpdateForm(forms.ModelForm):
    """Form to update logged-in student's profile data."""

    class Meta:
        model = User
        fields = (
            'email',
            'first_name',
            'last_name',
            'enrollment_number',
            'course',
            'branch',
            'year',
            'phone',
            'profile_picture',
            'registration',
            'valid'
        )
        widgets = {
            'email': forms.EmailInput(attrs={'class': 'form-control', 'readonly': 'readonly',  # This disables editing
                'placeholder': 'Email cannot be changed'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter first name'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter last name'}),
            'enrollment_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter enrollment number'}),
            'valid': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter valid'}),
            'registration': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter registration'}),
            'course': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter course'}),
            'branch': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter branch'}),
            'year': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter year'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter phone number'}),
            'profile_picture': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username1', 'enrollment_number', 'course', 'branch', 'year', 'phone', 'profile_picture','registration','valid']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'username1': forms.TextInput(attrs={'class': 'form-control'}),
            'enrollment_number': forms.TextInput(attrs={'class': 'form-control'}),
            'valid': forms.TextInput(attrs={'class': 'form-control'}),
            'registration': forms.TextInput(attrs={'class': 'form-control'}),
            'course': forms.TextInput(attrs={'class': 'form-control'}),
            'branch': forms.TextInput(attrs={'class': 'form-control'}),
            'year': forms.NumberInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
            'profile_picture': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }
    
class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'subject', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Your Name...', 'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Your Email...', 'class': 'form-control'}),
            'subject': forms.TextInput(attrs={'placeholder': 'Subject...', 'class': 'form-control'}),
            'message': forms.Textarea(attrs={'placeholder': 'Your Message...', 'class': 'form-control', 'rows': 5}),
        }