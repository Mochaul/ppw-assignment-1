from django import forms

class Add_Friend_Form(forms.Form):
    error_messages = {
        'required': 'Tolong isi input ini',
    }
    name_attrs = {
        'type': 'text',
        'class': 'todo-form-input',
        'placeholder':'Masukan nama teman kamu...'
    }
    url_attrs = {
        'type': 'text',
        'class': 'todo-form-input',
        'placeholder':'Masukan url tugas teman kamu...'
    }

    name = forms.CharField(label='Name', required=True, widget=forms.TextInput(attrs=name_attrs), error_messages=error_messages)
    url = forms.CharField(label='URL', required=True, widget=forms.TextInput(attrs=url_attrs), error_messages=error_messages)
