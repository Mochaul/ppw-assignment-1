from django import forms

class Add_Friend_Form(forms.Form):
    name_error_messages = {
        'required': 'Nama teman kamu wajib diisi',
    }
    url_error_messages = {
        'required': 'Url teman kamu wajib diisi',
    }
    name_attrs = {
        'type': 'text',
        'class': 'input-text',
        'placeholder':'Masukan nama teman kamu...'
    }
    url_attrs = {
        'type': 'text',
        'class': 'input-text-inline-button',
        'placeholder':'Masukan url tugas teman kamu...'
    }

    name = forms.CharField(label='Name', required=True, widget=forms.TextInput(attrs=name_attrs), error_messages=name_error_messages)
    url = forms.CharField(label='URL', required=True, widget=forms.TextInput(attrs=url_attrs), error_messages=url_error_messages)
