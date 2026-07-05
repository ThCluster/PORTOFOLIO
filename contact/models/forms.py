from django import forms

class ContactForm(forms.Form):
    
    full_name = forms.CharField(
        widget=forms.TextInput(attrs={"placeholder": "Full name", "class": "form-control"})
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={"placeholder": "Email address", "class": "form-control"})
    )
    phone_number = forms.CharField(
        required=False, # Optionnel si vous ne voulez pas obliger l'utilisateur à le remplir
        widget=forms.TextInput(attrs={"placeholder": "Phone number", "class": "form-control"})
    )
    message = forms.CharField(
        widget=forms.Textarea(attrs={"placeholder": "Message", "class": "form-control", "rows": 4})
    )
