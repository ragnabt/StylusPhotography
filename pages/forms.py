from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(
        max_length=200,
        label="",
        widget=forms.TextInput(attrs={
            "class": "input_field",
            "placeholder": "Név"
        })
    )

    email = forms.EmailField(
        max_length=200,
        label="",
        widget=forms.EmailInput(attrs={
            "class": "input_field",
            "placeholder": "Email"
        })
    )

    message = forms.CharField(
        max_length=1000,
        label="",
        widget=forms.Textarea(attrs={
            "placeholder": "Üzenet"
        })
    )
