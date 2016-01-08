from django import forms

class ContactForm(forms.Form):
    contact_name = forms.CharField(required=True, widget=forms.TextInput(attrs={'required': 'required', 'title': 'Insert your name', 'placeholder': 'Name...'}))
    contact_email = forms.EmailField(required=True, widget=forms.TextInput(attrs={'required': 'required', 'type': 'email', 'title': 'Insert your email', 'placeholder': 'Email...'}))
    content = forms.CharField(
        required=True,
        widget=forms.Textarea(attrs={'required': 'required', 'title': 'Insert your message', 'placeholder': 'Message'})
    )

    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        self.fields['contact_name'].label = "Your name:"
        self.fields['contact_email'].label = "Your email:"
        self.fields['content'].label = "What do you want to say?"