from django import forms

class Status_Form(forms.Form):
    error_messages = {
        'required': 'Tolong isi status',
    }
    description_attrs ={
    	'type':'text',
    	'rows':4,
    	'class':'status-form-textarea',
    	'placeholder':"What's on your mind?"
    }

    #name = forms.CharField(label='Nama', required=False, max_length=27, empty_value='Anonymous', widget=forms.TextInput(attrs=attrs))
    #email = forms.EmailField(required=False, widget=forms.EmailInput(attrs=attrs))
    status = forms.CharField(widget=forms.Textarea(attrs=description_attrs), required=True, label='')


class Comment_Form(forms.Form):
    error_messages ={
        'required':'Tolong isi comment'
    }
    description_attrs ={
        'type':'text',
        'rows':1,
        'class':'comment-form-textarea',
        'placeholder':'Please give a comment'
    }
    comment = forms.CharField(widget=forms.Textarea(attrs=description_attrs), required=True, label='')